# FILTER.UPDATE

Mass update all instances matching a condition.

## Syntax

```
FILTER.UPDATE > MODEL > ATTRIBUTE > OLD_VALUE > NEW_VALUE > OPERATOR(?)
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `MODEL` | Required | Model class |
| `ATTRIBUTE` | Required | Field to match on |
| `OLD_VALUE` | Required | Value to match |
| `NEW_VALUE` | Required | New value to set |
| `OPERATOR` | Optional | Comparison: `gt`, `lt`, `gte`, `lte` |

## Examples

### Simple Update

```sql
-- Change all Democracy regimes to Republic
FILTER.UPDATE > BALL > REGIME > Democracy > Republic
```

### With Operator

```sql
-- Set all balls with health > 100 to 100
FILTER.UPDATE > BALL > HEALTH > 100 > 100 > gt
```

## See Also

- [FILTER.DELETE](filter-delete.md) - Bulk deletion
- [FILTER.VIEW](filter-view.md) - View matching instances
- [UPDATE](update.md) - Update single instance
