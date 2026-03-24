# EVAL.REMOVE

Deletes a saved eval preset.

## Syntax

```
EVAL.REMOVE > NAME
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `NAME` | Required | Preset name to remove |

## Examples

### Remove a Preset

```sql
EVAL.REMOVE > old_script
```

## Behavior

- Permanently deletes the preset file
- Cannot be undone
- Preset must exist

## See Also

- [EVAL.SAVE](eval-save.md) - Create presets
- [EVAL.LIST](eval-list.md) - View all presets
- [EVAL.RUN](eval-run.md) - Execute presets
