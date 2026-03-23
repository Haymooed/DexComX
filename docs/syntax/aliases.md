# Aliases

DexComX supports built-in aliases for faster scripting.

## Available Aliases

| Alias | Full Command |
|-------|-------------|
| `set` | `UPDATE` |
| `show` | `VIEW` |
| `fields` | `ATTRIBUTES` |
| `rm` | `DELETE` |
| `del` | `DELETE` |
| `ls` | `LISTDIR` |

## Usage Examples

### set → UPDATE

```sql
-- Instead of:
UPDATE > BALL > France > HEALTH > 105

-- You can use:
set > BALL > France > HEALTH > 105
```

### show → VIEW

```sql
-- Instead of:
VIEW > BALL > France

-- You can use:
show > BALL > France
```

### rm / del → DELETE

```sql
-- Instead of:
DELETE > BALL > OldBall

-- You can use:
rm > BALL > OldBall
-- or:
del > BALL > OldBall
```

### ls → LISTDIR

```sql
-- Instead of:
FILE > LISTDIR > ./

-- You can use:
FILE.ls > ./
```

### fields → ATTRIBUTES

```sql
-- Instead of:
ATTRIBUTES > BALL

-- You can use:
fields > BALL
```

## Combining with Scoped Mode

Aliases work with scoped commands too:

```sql
-- FILE.ls instead of FILE.LISTDIR
FILE.ls > ./config

-- FILTER.rm instead of FILTER.DELETE
FILTER.rm > BALL > REGIME > Communist
```

## Benefits

- **Faster typing** - Less characters to type
- **More readable** - Familiar Unix-like commands (`ls`, `rm`)
- **Backward compatible** - Full commands still work

!!! tip
    Use aliases in interactive sessions for speed, and full commands in scripts for clarity.
