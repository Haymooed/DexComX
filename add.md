# UPDATE

Updates a model instance's attribute value.

## Syntax

```
UPDATE > MODEL > IDENTIFIER > ATTRIBUTE > VALUE
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `MODEL` | Required | Model class: `BALL`, `REGIME`, `ECONOMY`, `SPECIAL` |
| `IDENTIFIER` | Required | Name/identifier of the instance |
| `ATTRIBUTE` | Required | Field name to update |
| `VALUE` | Required | New value for the attribute |

## Examples

### Update Ball Health

```sql
UPDATE > BALL > France > HEALTH > 100
```

### Update Multiple Attributes

```sql
UPDATE > BALL > Germany > HEALTH > 105
UPDATE > BALL > Germany > ATTACK > 90
UPDATE > BALL > Germany > REGIME > Democracy
UPDATE > BALL > Germany > RARITY > 1.5
```

### Using Alias

```sql
-- set is alias for UPDATE
set > BALL > France > HEALTH > 105
```

### Update Foreign Keys

```sql
-- Link a ball to a regime
UPDATE > BALL > France > REGIME > Democracy
```

## Bulk Updates

For updating multiple instances at once, use `FILTER.UPDATE`:

```sql
FILTER.UPDATE > BALL > REGIME > Democracy > Republic
```

## See Also

- [CREATE](create.md) - Create instances
- [VIEW](view.md) - View current values
- [FILTER.UPDATE](filter-update.md) - Bulk updates
