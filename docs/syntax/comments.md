# Comments

DexComX supports single-line comments using `--` syntax.

## Syntax

```
-- This is a comment
```

## Usage

Comments are lines that start with `--` and are completely ignored during script execution.

## Examples

### Inline Documentation

```sql
-- Create a new ball for Germany
CREATE > BALL > Germany

-- Set health to 100
UPDATE > BALL > Germany > HEALTH > 100
```

### Section Headers

```sql
-- ==========================================
-- BALL SETUP SCRIPT
-- ==========================================

-- Create balls
CREATE > BALL > France
CREATE > BALL > Germany
CREATE > BALL > Spain

-- Configure health values
UPDATE > BALL > France > HEALTH > 100
UPDATE > BALL > Germany > HEALTH > 105
UPDATE > BALL > Spain > HEALTH > 95
```

### Disable Commands Temporarily

```sql
CREATE > BALL > TestBall
UPDATE > BALL > TestBall > HEALTH > 100
-- UPDATE > BALL > TestBall > ATTACK > 50
UPDATE > BALL > TestBall > REGIME > Democracy
```

The commented line will be skipped.

## Benefits

- **Document your scripts** - Explain what each section does
- **Disable commands** - Comment out lines instead of deleting them
- **Add headers** - Organize long scripts into sections
- **Leave notes** - Remind yourself why you made certain changes

## Rules

- Comments must start with `--` at the beginning of the line
- Leading whitespace before `--` is allowed
- Everything after `--` on that line is ignored
- Multi-line comments are not supported (use multiple `--` lines)

## Combined with Batch Execution

```sql
m.run
-- Batch script with comments
CREATE > BALL > Germany
UPDATE > BALL > Germany > HEALTH > 100
-- This next line is disabled
-- DELETE > BALL > OldBall
UPDATE > BALL > Germany > ATTACK > 90
```

## See Also

- [Batch Execution](batch.md) - Run multi-line scripts
- [Syntax Overview](overview.md) - Command structure
