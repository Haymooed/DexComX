# FILE.READ

Sends a file as a Discord attachment.

## Syntax

```
FILE.READ > PATH
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `PATH` | Required | File path relative to bot directory |

## Examples

### Read Config File

```sql
FILE.READ > ./config.json
```

### Read From Subdirectory

```sql
FILE.READ > ./data/export.csv
```

## Behavior

- Sends file as Discord attachment
- File must exist and be readable
- Respects Discord file size limits (25MB)

## See Also

- [FILE.WRITE](file-write.md) - Write to files
- [FILE.LISTDIR](file-listdir.md) - List directory contents
