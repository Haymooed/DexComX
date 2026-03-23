# Batch Execution

Execute multiple DexComX commands in a single message using batch mode.

## Syntax

```
b.run
COMMAND1 > ARG1 > ARG2
COMMAND2 > ARG1 > ARG2
COMMAND3 > ARG1 > ARG2
```

## How It Works

Prefix your multi-line script with `b.run` (or `o.run`) and DexComX will execute each line sequentially.

## Examples

### Basic Batch Script

```sql
b.run
CREATE > BALL > Germany
UPDATE > BALL > Germany > HEALTH > 100
UPDATE > BALL > Germany > ATTACK > 90
UPDATE > BALL > Germany > REGIME > Democracy
```

### With Comments

```sql
b.run
-- Create new balls
CREATE > BALL > France
CREATE > BALL > Germany

-- Configure France
UPDATE > BALL > France > HEALTH > 100
UPDATE > BALL > France > ATTACK > 85

-- Configure Germany
UPDATE > BALL > Germany > HEALTH > 105
UPDATE > BALL > Germany > ATTACK > 90
```

### Mixed Commands

```sql
b.run
-- Filter operations
FILTER.UPDATE > BALL > REGIME > Democracy > Republic
FILTER.DELETE > BALL > REGIME > Communist

-- Create new ball
CREATE > BALL > NewCountry

-- File operations
FILE.READ > ./config.json
```

## Error Handling

If any command in the batch fails:
- DexComX continues executing remaining commands
- All errors are collected and shown at the end
- Successful commands show ✅ reaction

## Benefits

- **Paste entire scripts** - Copy/paste from text files
- **Atomic operations** - Run related commands together
- **Script sharing** - Share full workflows with others
- **Version control** - Save scripts in git

## Alternative: Single Command Mode

Without `b.run`, send one command per message:

```
run CREATE > BALL > Germany
```

```
run UPDATE > BALL > Germany > HEALTH > 100
```

Batch mode is faster for multiple commands.

## Tips

1. **Test individual commands first** - Verify syntax before batching
2. **Use comments liberally** - Document what each section does
3. **Save scripts as files** - Keep reusable scripts in your project
4. **Check for errors** - Review all error messages at the end

## See Also

- [Comments](comments.md) - Document your batch scripts
- [Syntax Overview](overview.md) - Command structure
- [Aliases](aliases.md) - Speed up batch scripts
