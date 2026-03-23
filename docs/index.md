# DexComX

DexComX is a script-driven admin toolkit for BallsDex that lets owners create, update, filter, view, and remove model data quickly from Discord.

!!! info "Credits"
    **Originally created by [Cayla (DexScript)](https://github.com/Caylies/DexScript)** — DexComX builds upon the original DexScript foundation with improved command parsing, speed aliases, and extension management.

## Installation

Add to your `config/extra.toml`:

```toml
[[ballsdex.packages]]
location = "git+https://github.com/Haymooed/DexComX.git"
path = "dexscript_app"
enabled = true
editable = false
```

Then restart your BallsDex bot.

## Features

- **Speed Aliases**: `set`, `show`, `rm`, `ls`, `fields` — faster commands
- **Scoped Commands**: `FILTER.UPDATE > BALL > REGIME > Democracy > Republic`
- **Bulk Filter Operations**: Mass update, delete, or view rows
- **Eval Presets**: Save and run Python eval scripts
- **File System Tools**: Read, write, clear, list, and delete files
- **Extension Manager**: Install BallsDex packages directly from Discord
- **Batch Execution**: Paste entire scripts with `b.run` prefix
- **Comment Support**: Lines starting with `--` are ignored

## Quick Start

All commands are **owner-only**. Execute scripts with:

```
run <script>
```

or

```
o.run <script>
```

### Example: Create a Ball

```sql
CREATE > BALL > Germany
UPDATE > BALL > Germany > HEALTH > 100
UPDATE > BALL > Germany > ATTACK > 90
UPDATE > BALL > Germany > REGIME > Democracy
```

### Example: Bulk Operations

```sql
-- Change all Democracy regimes to Republic
FILTER.UPDATE > BALL > REGIME > Democracy > Republic

-- View all balls with health > 100
FILTER.VIEW > BALL > HEALTH > 100 > gt
```

### Example: Using Aliases

```sql
-- set is alias for UPDATE
set > BALL > France > HEALTH > 105

-- show is alias for VIEW
show > BALL > France
```

## Available Models

- `BALL`
- `REGIME`
- `ECONOMY`
- `SPECIAL`

## Next Steps

- Learn about [Syntax](syntax/overview.md)
- Explore [Commands](commands/create.md)
- Manage [Extensions](extensions/overview.md)
