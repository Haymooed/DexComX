# FILTER.VIEW

Display all instances matching a condition.

## Syntax

```
FILTER.VIEW > MODEL > ATTRIBUTE > VALUE > OPERATOR(?)
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `MODEL` | Required | Model class |
| `ATTRIBUTE` | Required | Field to match on |
| `VALUE` | Required | Value to match |
| `OPERATOR` | Optional | Comparison: `gt`, `lt`, `gte`, `lte` |

## Examples

### Simple View

```sql
-- View all balls with Democracy regime
FILTER.VIEW > BALL > REGIME > Democracy
```

### With Operator

```sql
-- View all balls with health > 100
FILTER.VIEW > BALL > HEALTH > 100 > gt
```

## See Also

- [FILTER.UPDATE](filter-update.md) - Bulk updates
- [FILTER.DELETE](filter-delete.md) - Bulk deletion
- [VIEW](view.md) - View single instance
