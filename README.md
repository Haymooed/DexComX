# DexComX

DexComX is the rebranded successor to DexScript-V3, maintained by **haymooed**.

It is a script-driven admin toolkit for BallsDex that lets owners create, update, filter, view, and remove model data quickly from Discord.

## What changed in DexComX

DexComX changes how commands are parsed and executed:

- You can now separate arguments with any of these separators:
  - `>`
  - `::`
  - `=>`
- You can run commands in **classic mode** or **scoped mode**.
- You can use lightweight aliases (`set`, `show`, `rm`, `ls`, `fields`) for faster commanding.

## Command format

### 1) Classic mode (legacy compatible)

```sql
UPDATE > BALL > France > HEALTH > 100
```

### 2) Scoped mode (new)

```sql
FILTER.UPDATE :: BALL :: REGIME :: Democracy :: Republic
```

### 3) Slash-style action token (new)

```sql
/show => BALL => France => HEALTH
```

## Full command reference

> Notes:
> - `MODEL` is typically one of: `BALL`, `REGIME`, `ECONOMY`, `SPECIAL`
> - Optional arguments are marked with `(?)`

---

### Global commands

#### CREATE
- `CREATE > MODEL > IDENTIFIER`
- Creates a model instance.

#### DELETE
- `DELETE > MODEL > IDENTIFIER`
- Deletes a model instance by identifier.

#### UPDATE
- `UPDATE > MODEL > IDENTIFIER > ATTRIBUTE > VALUE(?)`
- Updates one attribute on one model instance.
- If `VALUE` is omitted and the target field is an image-like field, attached files are used.

#### VIEW
- `VIEW > MODEL > IDENTIFIER > ATTRIBUTE(?)`
- Shows one field, or all visible fields when `ATTRIBUTE` is omitted.

#### ATTRIBUTES
- `ATTRIBUTES > MODEL > FILTER(?)`
- Lists editable fields.
- Filters:
  - `NULL`
  - `VALID`

---

### Filter commands

#### FILTER.UPDATE
- `FILTER > UPDATE > MODEL > ATTRIBUTE > OLD_VALUE > NEW_VALUE > OPERATOR(?)`
- Bulk-updates matching rows.

#### FILTER.DELETE
- `FILTER > DELETE > MODEL > ATTRIBUTE > VALUE > OPERATOR(?)`
- Bulk-deletes matching rows.

#### FILTER.VIEW
- `FILTER > VIEW > MODEL > ATTRIBUTE > VALUE > OPERATOR(?)`
- Lists matching row identifiers.

---

### Eval preset commands

#### EVAL.SAVE
- `EVAL > SAVE > NAME`
- Prompts for eval content and saves it as a preset.

#### EVAL.REMOVE
- `EVAL > REMOVE > NAME`
- Deletes a preset.

#### EVAL.LIST
- `EVAL > LIST`
- Lists presets.

#### EVAL.RUN
- `EVAL > RUN > NAME`
- Executes a saved preset.

---

### File system commands

#### FILE.READ
- `FILE > READ > FILE_PATH`
- Sends a file.

#### FILE.WRITE
- `FILE > WRITE > FILE_PATH`
- Writes from the attached file contents to the path.

#### FILE.CLEAR
- `FILE > CLEAR > FILE_PATH`
- Empties a file.

#### FILE.LISTDIR
- `FILE > LISTDIR > FILE_PATH(?)`
- Lists directory contents.

#### FILE.DELETE
- `FILE > DELETE > FILE_PATH`
- Deletes a file or directory.

---

### Template helper commands

#### TEMPLATE.CREATE
- `TEMPLATE > CREATE > MODEL > ARGUMENT(?)`
- Sends starter command templates for model setup.

## Aliases

DexComX supports built-in aliases for faster scripting:

- `set` → `update`
- `show` → `view`
- `fields` → `attributes`
- `rm` / `del` → `delete`
- `ls` → `listdir`

Examples:

```sql
set > BALL > France > HEALTH > 105
show :: BALL :: France
FILE.ls => ./
```

## Comment lines

Any line starting with `--` is treated as a comment and ignored.

```sql
-- this line will be ignored
CREATE > BALL > NewCountry
```

## Ownership and execution

- Use the Discord owner-only command:
  - `run <script>`
- Paste scripts in code blocks or plain text; markdown wrappers are stripped automatically.

### Sending one big message

DexComX now accepts batch pastes where each line starts with `o.run` (or `run`), so you can send a full setup script in one message:

b.run
```sql
CREATE > BALL > A
UPDATE > BALL > A > REGIME > Communist
UPDATE > BALL > A > HEALTH > 100
UPDATE > BALL > A > ATTACK > 90
```

Lines wrapped with single backticks are cleaned automatically before parsing.

## Maintainer

- Creator / Maintainer: **haymooed**
