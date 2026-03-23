# FILE.CLEAR

Clears all content from a file (makes it empty).

## Syntax

```
FILE.CLEAR > PATH
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `PATH` | Required | File path to clear |

## Examples

### Clear Log File

```sql
FILE.CLEAR > ./logs/debug.log
```

## Behavior

- Empties the file (0 bytes)
- File must already exist
- Does not delete the file

## See Also

- [FILE.DELETE](file-delete.md) - Delete files completely
- [FILE.WRITE](file-write.md) - Write new content
