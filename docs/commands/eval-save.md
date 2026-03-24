# EVAL.SAVE

Saves a Python eval preset for later execution.

## Syntax

```
EVAL.SAVE > NAME
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `NAME` | Required | Preset name (max 100 chars) |

## Workflow

1. Run `EVAL.SAVE > my_preset`
2. Bot asks: "Please send the eval command below..."
3. Send your Python eval code
4. Preset is saved

## Examples

### Save a Preset

```
run EVAL.SAVE > calculate_stats
```

Then send:
```python
total_balls = await Ball.objects.count()
print(f"Total balls: {total_balls}")
```

## Behavior

- Preset saved to `eval_presets/NAME.py`
- 100-character name limit
- Overwrites not allowed (prevents accidents)

## See Also

- [EVAL.RUN](eval-run.md) - Execute saved presets
- [EVAL.LIST](eval-list.md) - View all presets
- [EVAL.REMOVE](eval-remove.md) - Delete presets
