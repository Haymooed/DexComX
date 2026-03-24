import inspect
import re
import traceback
from dataclasses import dataclass
from dataclasses import field as datafield
from typing import Any

from dateutil.parser import parse as parse_date

from . import commands
from .utils import Types, Utils, config

TOKEN_SPLIT_RE = re.compile(r"\s*(?:>|::|=>)\s*")
RUN_PREFIX_RE = re.compile(r"^(?:o\.)?run\b", re.IGNORECASE)


@dataclass
class Value:
    name: str
    type: Types = Types.DEFAULT
    value: Any = None
    extra_data: list = datafield(default_factory=list)

    def __str__(self):
        return self.name


class DexScriptParser:
    """This class is used to parse DexComX script into Python code."""

    def __init__(self, ctx, bot):
        self.ctx = ctx
        self.bot = bot

        self.command_classes = inspect.getmembers(
            commands,
            lambda o: (
                inspect.isclass(o)
                and issubclass(o, commands.DexCommand)
                and not issubclass(o, commands.Global)
                and o.__name__ != "DexCommand"
            ),
        )

        self.global_methods = [x for x in dir(commands.Global) if not x.startswith("__")]
        self.class_map = {self.normalize_token(name): value for name, value in self.command_classes}
        self.global_map = {self.normalize_token(name): name for name in self.global_methods}
        self.aliases = {
            "ls": "listdir",
            "rm": "delete",
            "del": "delete",
            "set": "update",
            "show": "view",
            "fields": "attributes",
        }

    @staticmethod
    def normalize_token(value: str) -> str:
        value = value.strip().lower()
        if value.startswith("/"):
            value = value[1:]
        return value.replace("_", "").replace("-", "")

    def create_value(self, line):
        value = Value(line)
        value.value = line

        lower = line.lower()
        type_dict = {
            Types.METHOD: self.normalize_token(line) in self.global_map,
            Types.CLASS: self.normalize_token(line) in self.class_map,
            Types.MODEL: lower in Utils.models(True, key=str.lower),
            Types.DATETIME: Utils.is_date(lower) and lower.count("-") >= 2,
            Types.BOOLEAN: lower in ["true", "false"],
        }

        for key, operation in type_dict.items():
            if operation is False:
                continue
            value.type = key
            break

        match value.type:
            case Types.MODEL:
                model = Utils.fetch_model(line)
                if model is None:
                    raise Exception(f"'{line}' is not a valid model")

                string_key = Utils.extract_str_attr(model)
                value.name = model.__name__
                value.value = model
                value.extra_data.append(string_key)
            case Types.BOOLEAN:
                value.value = lower == "true"
            case Types.DATETIME:
                value.value = parse_date(line)

        return value

    def error(self, message, log):
        return (message, log)[config.debug]

    def clean_line(self, line: str) -> str:
        """Normalize one script line so big pasted batches execute reliably."""
        line = line.strip().strip("`")

        if not line:
            return ""

        # Allow users to paste chat-style commands like: o.run UPDATE > BALL > ...
        line = RUN_PREFIX_RE.sub("", line, count=1).strip()

        # Ignore lines that only contain a command prefix.
        if line in {"", "."}:
            return ""

        return line

    def resolve_call(self, token: Value):
        raw = token.name
        normalized = self.normalize_token(raw)

        if "." in raw:
            class_name, method_name = raw.split(".", 1)
            class_obj = self.class_map.get(self.normalize_token(class_name))
            method = self.aliases.get(self.normalize_token(method_name), self.normalize_token(method_name))
            if class_obj is not None and hasattr(class_obj, method):
                return class_obj, method

        method_name = self.aliases.get(normalized, normalized)

        if method_name in self.global_map:
            return commands.Global, self.global_map[method_name]
        if normalized in self.class_map:
            return self.class_map[normalized], None

        return None, None

    async def execute(self, code: str, run_commands=True):
        shared_instance = commands.Shared(self.ctx.message.attachments)
        split_code = [self.clean_line(x) for x in code.split("\n")]
        split_code = [x for x in split_code if x]

        parsed_code = [
            [self.create_value(s.strip()) for s in TOKEN_SPLIT_RE.split(line) if s.strip()]
            for line in split_code
            if not line.strip().startswith("--")
        ]

        if not run_commands:
            return parsed_code

        errors = []

        for index, line2 in enumerate(parsed_code, start=1):
            if line2 == []:
                continue

            command_class, method_name = self.resolve_call(line2[0])
            if command_class is None:
                errors.append(
                    self.error(
                        f"Line {index}: '{line2[0].name}' is not a valid command.",
                        traceback.format_exc(),
                    )
                )
                continue

            line2.pop(0)

            if method_name is None:
                if not line2:
                    errors.append(
                        self.error(
                            f"Line {index}: missing method after '{command_class.__name__}'.",
                            traceback.format_exc(),
                        )
                    )
                    continue
                method_name = self.aliases.get(
                    self.normalize_token(line2[0].name), self.normalize_token(line2[0].name)
                )
                line2.pop(0)

            class_loaded = command_class(self.bot, shared_instance)
            class_loaded.__loaded__()

            method_call = getattr(class_loaded, method_name, None)
            if method_call is None:
                errors.append(
                    self.error(
                        f"Line {index}: '{method_name}' is not a valid method for '{command_class.__name__}'.",
                        traceback.format_exc(),
                    )
                )
                continue

            try:
                await method_call(self.ctx, *line2)
            except TypeError:
                errors.append(
                    self.error(
                        f"Line {index}: argument missing when calling '{method_name}'.",
                        traceback.format_exc(),
                    )
                )

        if errors:
            return "\n".join(str(e) for e in errors)
