# FILE.LISTDIR

Lists all files and directories in a path.

## Syntax

```
FILE.LISTDIR > PATH(?)
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `PATH` | Optional | Directory path (defaults to current directory) |

## Examples

### List Current Directory

```sql
FILE.LISTDIR
```

### List Specific Directory

```sql
FILE.LISTDIR > ./data
```

### Using Alias

```sql
-- ls is alias for LISTDIR
FILE.ls > ./config
```

## Behavior

- Shows files and subdirectories
- Returns as paginated list
- Respects Discord message limits

## See Also

- [FILE.READ](file-read.md) - Read file contents
- [FILE.DELETE](file-delete.md) - Delete files
