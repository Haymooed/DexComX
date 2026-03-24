# FILE.DELETE

Deletes a file or directory permanently.

## Syntax

```
FILE.DELETE > PATH
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `PATH` | Required | File or directory path |

## Examples

### Delete File

```sql
FILE.DELETE > ./temp/old_data.json
```

### Delete Directory

```sql
FILE.DELETE > ./temp
```

## Behavior

- Permanently deletes files or directories
- Directories are deleted recursively
- Cannot be undone

!!! warning
    This action is permanent. Always verify the path before deleting.

## See Also

- [FILE.CLEAR](file-clear.md) - Clear file without deleting
- [FILE.LISTDIR](file-listdir.md) - List files
