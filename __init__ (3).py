# DexComX

DexComX is a script-driven admin toolkit for BallsDex that lets owners create, update, filter, view, and remove model data quickly from Discord.

**Originally created by [Cayla (DexScript)](https://github.com/Caylies/DexScript)** — DexComX builds upon the original DexScript foundation with modernized syntax and improved command parsing.

## Quick Install

Add to your `config/extra.toml`:

```toml
[[ballsdex.packages]]
location = "git+https://github.com/Haymooed/DexComX.git"
path = "dexscript_app"
enabled = true
editable = false
```

Then restart your BallsDex bot.

## Documentation

Full command reference and interactive builder: **https://haymooed.github.io/DexComX/**

---

## What's New in DexComX

- **Multiple separators**: Use `>`, `::`, or `=>` interchangeably
- **Scoped mode**: `FILTER.UPDATE :: BALL :: REGIME :: Democracy :: Republic`
- **Speed aliases**: `set`, `show`, `rm`, `ls`, `fields`
- **Batch execution**: Paste entire scripts with `m.run` prefix
- **Comment support**: Lines starting with `--` are ignored

## Command Format

### Classic Mode (legacy compatible)
```sql
UPDATE > BALL > France > HEALTH > 100
```

### Scoped Mode
```sql
FILTER.UPDATE :: BALL :: REGIME :: Democracy :: Republic
```

### Slash-Style
```sql
/show => BALL => France => HEALTH
```

## Core Commands

| Command | Syntax | Description |
|---------|--------|-------------|
| **CREATE** | `CREATE > MODEL > IDENTIFIER` | Creates a model instance |
| **DELETE** | `DELETE > MODEL > IDENTIFIER` | Deletes a model instance |
| **UPDATE** | `UPDATE > MODEL > ID > ATTRIBUTE > VALUE` | Updates one attribute |
| **VIEW** | `VIEW > MODEL > ID > ATTRIBUTE(?)` | Shows field(s) |
| **ATTRIBUTES** | `ATTRIBUTES > MODEL > FILTER(?)` | Lists editable fields |

### Filter Commands (Bulk Operations)

| Command | Syntax |
|---------|--------|
| **FILTER.UPDATE** | `FILTER > UPDATE > MODEL > ATTR > OLD > NEW > OP(?)` |
| **FILTER.DELETE** | `FILTER > DELETE > MODEL > ATTR > VALUE > OP(?)` |
| **FILTER.VIEW** | `FILTER > VIEW > MODEL > ATTR > VALUE > OP(?)` |

### File System Commands

| Command | Syntax |
|---------|--------|
| **FILE.READ** | `FILE > READ > PATH` |
| **FILE.WRITE** | `FILE > WRITE > PATH` |
| **FILE.CLEAR** | `FILE > CLEAR > PATH` |
| **FILE.LISTDIR** | `FILE > LISTDIR > PATH(?)` |
| **FILE.DELETE** | `FILE > DELETE > PATH` |

### Eval Presets

| Command | Syntax |
|---------|--------|
| **EVAL.SAVE** | `EVAL > SAVE > NAME` |
| **EVAL.REMOVE** | `EVAL > REMOVE > NAME` |
| **EVAL.LIST** | `EVAL > LIST` |
| **EVAL.RUN** | `EVAL > RUN > NAME` |

## Aliases

```
set     → update
show    → view
fields  → attributes
rm/del  → delete
ls      → listdir
```

## Batch Execution

```
m.run
CREATE > BALL > Germany
UPDATE > BALL > Germany > HEALTH > 100
UPDATE > BALL > Germany > ATTACK > 90
UPDATE > BALL > Germany > REGIME > Democracy
```

## Available Models

- `BALL`
- `REGIME`
- `ECONOMY`
- `SPECIAL`

## Usage

All commands are **owner-only**. Execute with:
```
m.run <script>
```

## Credits

- **Original Creator**: [Cayla](https://github.com/Caylies/DexScript) - Created DexScript
- **Current Maintainer**: [haymooed](https://github.com/Haymooed) - DexComX improvements

## License

This project builds upon the original DexScript. Please respect the original creator's work.
