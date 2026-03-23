# Syntax Overview

DexComX uses a simple, command-based syntax with the `>` separator.

## Basic Format

```
COMMAND > ARGUMENT1 > ARGUMENT2 > ARGUMENT3
```

## Scoped Mode

Use dot-notation to scope to a command class:

```sql
FILTER.UPDATE > BALL > REGIME > Democracy > Republic
FILE.READ > ./config.json
```

## Slash-Style

You can prefix commands with `/` for readability:

```sql
/show > BALL > France > HEALTH
/rm > BALL > OldBall
```

## Command Structure

### Global Commands

```
UPDATE > BALL > France > HEALTH > 100
VIEW > BALL > France
DELETE > BALL > OldBall
```

### Scoped Commands

```
FILTER.UPDATE > BALL > REGIME > Democracy > Republic
FILE.READ > ./settings.json
EVAL.RUN > my_preset
```

## Models

DexComX works with these BallsDex models:

- **BALL** - Country balls/collectibles
- **REGIME** - Political regimes
- **ECONOMY** - Economic systems
- **SPECIAL** - Special items

## Optional Arguments

Some commands have optional arguments marked with `(?)`:

```
VIEW > BALL > France > HEALTH(?)
ATTRIBUTES > BALL > FILTER(?)
```

If omitted, the command uses default behavior.

## Examples

### Simple Update

```sql
UPDATE > BALL > France > HEALTH > 100
```

### Scoped Filter

```sql
FILTER.VIEW > BALL > REGIME > Democracy
```

### File Operation

```sql
FILE.READ > ./config.json
```

## Next Steps

- [Aliases](aliases.md) - Speed up commands with shortcuts
- [Comments](comments.md) - Document your scripts
- [Batch Execution](batch.md) - Run multiple commands at once
