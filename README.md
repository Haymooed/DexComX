# DexComX

DexComX is a script-driven admin toolkit for BallsDex that lets owners create, update, filter, view, and remove model data quickly from Discord.

**Originally created by [Cayla (DexScript)](https://github.com/Caylies/DexScript)** — DexComX builds upon the original DexScript foundation with improved command parsing, speed aliases, and extension management.

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

Full command reference: **https://haymooed.github.io/DexComX/**

---

## What's New in DexComX

- **Scoped commands**: `FILTER.UPDATE > BALL > REGIME > Democracy > Republic`
- **Speed aliases**: `set`, `show`, `rm`, `ls`, `fields`
- **Batch execution**: Paste entire scripts with `b.run` prefix
- **Comment support**: Lines starting with `--` are ignored
- **🆕 Extension Manager**: Install BallsDex packages directly from Discord

## Extension Manager

Manage BallsDex packages without editing config files!

### Add Extension
```
/admin extension add https://github.com/User/Package.git
```

### Remove Extension
```
/admin extension remove package_name
```

### List Installed Extensions
```
/admin extension list
```

### Update Extension
```
/admin extension update package_name
```

### How It Works

1. **Add**: Downloads the package from git, adds it to `config/extra.toml`, and attempts to load it
2. **Remove**: Removes from config and unloads the extension
3. **List**: Shows all installed packages with their URLs and status
4. **Update**: Pulls latest version from git and reinstalls

**Note:** Some changes may require a bot restart to fully apply.

---

## Command Format

### Standard Mode
```sql
UPDATE > BALL > France > HEALTH > 100
```

### Scoped Mode
```sql
FILTER.UPDATE > BALL > REGIME > Democracy > Republic
```

### Slash-Style
```sql
/show > BALL > France > HEALTH
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
b.run
```sql
CREATE > BALL > Germany
UPDATE > BALL > Germany > HEALTH > 100
UPDATE > BALL > Germany > ATTACK > 90
UPDATE > BALL > Germany > REGIME > Democracy
```
```

## Available Models

- `BALL`
- `REGIME`
- `ECONOMY`
- `SPECIAL`

## Usage

All commands are **owner-only**. Execute with:
```
run <script>
```
or
```
o.run <script>
```

## Examples

### Creating a New Ball
```sql
CREATE > BALL > Germany
UPDATE > BALL > Germany > HEALTH > 100
UPDATE > BALL > Germany > ATTACK > 90
UPDATE > BALL > Germany > REGIME > Democracy
UPDATE > BALL > Germany > RARITY > 1.0
```

### Bulk Operations
```sql
-- Change all Democracy regimes to Republic
FILTER.UPDATE > BALL > REGIME > Democracy > Republic

-- View all balls with health > 100
FILTER.VIEW > BALL > HEALTH > 100 > gt

-- Delete all balls with Communist regime
FILTER.DELETE > BALL > REGIME > Communist
```

### Using Aliases
```sql
-- set is alias for UPDATE
set > BALL > France > HEALTH > 105

-- show is alias for VIEW
show > BALL > France

-- FILE.ls is alias for FILE.LISTDIR
FILE.ls > ./
```

### Managing Extensions
```sql
-- Install a new package
/admin extension add https://github.com/Haymooed/BallsDex-Merchant-Package.git

-- List all packages
/admin extension list

-- Update a package
/admin extension update ballsdex_merchant_package

-- Remove a package
/admin extension remove ballsdex_merchant_package
```

## Requirements

- Python 3.10+
- BallsDex v3+
- toml library (for extension manager)

## Credits

- **Original Creator**: [Cayla](https://github.com/Caylies/DexScript) - Created DexScript
- **Current Maintainer**: [haymooed](https://github.com/Haymooed) - DexComX improvements

## License

This project builds upon the original DexScript. Please respect the original creator's work.