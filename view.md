# TEMPLATE.CREATE

Generates a pre-filled template for creating model instances.

## Syntax

```
TEMPLATE.CREATE > MODEL > IDENTIFIER(?)
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `MODEL` | Required | Model class (currently only `BALL` supported) |
| `IDENTIFIER` | Optional | Name for the instance (defaults to `...`) |

## Examples

### Generate Ball Template

```sql
TEMPLATE.CREATE > BALL > Germany
```

**Output:**
```sql
CREATE > BALL > Germany
UPDATE > BALL > Germany > REGIME > ...
UPDATE > BALL > Germany > HEALTH > ...
UPDATE > BALL > Germany > ATTACK > ...
UPDATE > BALL > Germany > RARITY > ...
UPDATE > BALL > Germany > EMOJI_ID > ...
UPDATE > BALL > Germany > CREDITS > ...
UPDATE > BALL > Germany > CAPACITY_NAME > ...
UPDATE > BALL > Germany > CAPACITY_DESCRIPTION > ...
```

### Generic Template

```sql
TEMPLATE.CREATE > BALL
```

Uses `...` as placeholder for all values.

## Behavior

- Generates ready-to-paste script
- Includes all common attributes
- Replace `...` with actual values

## Workflow

1. Generate template
2. Copy output
3. Replace `...` placeholders
4. Paste into `m.run` batch execution

## See Also

- [CREATE](create.md) - Create instances
- [UPDATE](update.md) - Update attributes
- [Batch Execution](../syntax/batch.md) - Run templates
