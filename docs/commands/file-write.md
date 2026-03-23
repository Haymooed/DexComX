# FILE.WRITE

Writes Discord attachment content to a file.

## Syntax

```
FILE.WRITE > PATH
```

**Requires:** Attach a file to the message

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `PATH` | Required | Destination file path |

## Examples

### Write to Config

```sql
FILE.WRITE > ./config.json
```

*(Attach config.json file to message)*

## Behavior

- Overwrites existing file
- Creates file if it doesn't exist
- File content comes from Discord attachment

## See Also

- [FILE.READ](file-read.md) - Read files
- [FILE.CLEAR](file-clear.md) - Clear file contents
