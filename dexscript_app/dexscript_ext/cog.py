import traceback
from typing import TYPE_CHECKING

import discord
from ballsdex.settings import settings
from discord.ext import commands

from .parser import DexScriptParser
from .utils import Utils, config

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot

__version__ = "1.0"


class DexScript(commands.Cog):
    """
    DexComX commands
    """

    def __init__(self, bot: "BallsDexBot"):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def run(self, ctx: commands.Context, *, code: str):
        """
        Executes DexComX code.

        Parameters
        ----------
        code: str
          The code you want to execute.
        """
        body = Utils.remove_code_markdown(code)

        dexscript_instance = DexScriptParser(ctx, self.bot)

        try:
            result = await dexscript_instance.execute(body)
        except Exception as error:
            full_error = traceback.format_exc() if config.debug else error
            await ctx.send(f"```ERROR: {full_error}```")
            return
        else:
            if result is not None:
                await ctx.send(f"```ERROR: {result}```")
                return

            await ctx.message.add_reaction("✅")

    @commands.command()
    @commands.is_owner()
    async def about(self, ctx: commands.Context):
        """
        Displays information about DexComX.
        """
        guide_link = "https://github.com/Dexscript-V3/Dexscript-V3/blob/main/README.md"

        description = (
            "DexComX is a rebranded scripting toolkit for Ballsdex created by haymooed. "
            "It modernizes command execution with aliases and multi-separator parsing so scripts are easier to write and maintain. "
            "Use it for bulk content operations across balls, regimes, economy, and specials.\n\n"
            f"Read the [DexComX command reference](<{guide_link}>) for full syntax and examples."
        )

        embed = discord.Embed(
            title="DexComX",
            description=description,
            color=discord.Color.from_str("#03BAFC"),
        )

        embed.set_thumbnail(
            url="https://raw.githubusercontent.com/Dotsian/DexScript/refs/heads/dev/assets/DexScriptLogo.png"
        )
        embed.set_footer(text=f"DexComX {__version__}")

        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def setting(self, ctx: commands.Context, setting: str, value: str | None = None):
        """
        Changes a setting based on the value provided.

        Parameters
        ----------
        setting: str
          The setting you want to toggle.
        value: str | None
          The value you want to set the setting to.
        """
        setting = setting.lower()

        if setting not in vars(config):
            await ctx.send(f"`{setting}` is not a valid setting.")
            return

        setting_value = vars(config)[setting]
        new_value = value

        if isinstance(setting_value, bool):
            new_value = bool(value) if value else not setting_value

        setattr(config, setting, new_value)

        await ctx.send(f"`{setting}` has been set to `{new_value}`")
