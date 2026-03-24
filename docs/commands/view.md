# VIEW

Displays an attribute or all attributes of a model instance.

## Syntax

```
VIEW > MODEL > IDENTIFIER > ATTRIBUTE(?)
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `MODEL` | Required | Model class |
| `IDENTIFIER` | Required | Instance name |
| `ATTRIBUTE` | Optional | Specific field to view (omit to see all) |

## Examples

### View All Attributes

```sql
VIEW > BALL > France
```

**Output:**
```
country: France
health: 100
attack: 90
regime_id: 1
rarity: 1.0
...
```

### View Specific Attribute

```sql
VIEW > BALL > France > HEALTH
```

**Output:**
```
100
```

### Using Alias

```sql
-- show is alias for VIEW
show > BALL > France
show > BALL > France > HEALTH
```

## See Also

- [UPDATE](update.md) - Modify values
- [ATTRIBUTES](attributes.md) - List available fields
- [FILTER.VIEW](filter-view.md) - View multiple instances
