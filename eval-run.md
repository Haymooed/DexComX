# EVAL.LIST

Lists all saved eval presets.

## Syntax

```
EVAL.LIST
```

## Examples

### List Presets

```sql
EVAL.LIST
```

**Output:**
```
calculate_stats.py
export_data.py
update_regimes.py
```

## Behavior

- Shows all preset names
- Presets stored in `eval_presets/` directory
- Returns "no presets" if folder is empty

## See Also

- [EVAL.SAVE](eval-save.md) - Create presets
- [EVAL.RUN](eval-run.md) - Execute presets
- [EVAL.REMOVE](eval-remove.md) - Delete presets
