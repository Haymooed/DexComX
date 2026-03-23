# FILTER.DELETE

Mass delete all instances matching a condition.

## Syntax

```
FILTER.DELETE > MODEL > ATTRIBUTE > VALUE > OPERATOR(?)
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `MODEL` | Required | Model class |
| `ATTRIBUTE` | Required | Field to match on |
| `VALUE` | Required | Value to match |
| `OPERATOR` | Optional | Comparison: `gt`, `lt`, `gte`, `lte` |

## Examples

### Simple Delete

```sql
-- Delete all balls with Communist regime
FILTER.DELETE > BALL > REGIME > Communist
```

### With Operator

```sql
-- Delete all balls with health < 50
FILTER.DELETE > BALL > HEALTH > 50 > lt
```

## See Also

- [FILTER.UPDATE](filter-update.md) - Bulk updates
- [FILTER.VIEW](filter-view.md) - View before deleting
- [DELETE](delete.md) - Delete single instance
