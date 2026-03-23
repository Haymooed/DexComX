# EVAL.RUN

Executes a saved eval preset.

## Syntax

```
EVAL.RUN > NAME
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `NAME` | Required | Preset name to execute |

## Examples

### Run a Preset

```sql
EVAL.RUN > calculate_stats
```

## Behavior

- Executes Python code from the preset
- Uses bot's eval command internally
- Shows ✅ on success, error message on failure

## See Also

- [EVAL.SAVE](eval-save.md) - Create presets
- [EVAL.LIST](eval-list.md) - View all presets
- [EVAL.REMOVE](eval-remove.md) - Delete presets
