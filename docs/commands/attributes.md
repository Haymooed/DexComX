# ATTRIBUTES

Lists all editable attributes of a model.

## Syntax

```
ATTRIBUTES > MODEL > FILTER(?)
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `MODEL` | Required | Model class |
| `FILTER` | Optional | Filter type: `null`, `valid` |

## Examples

### List All Attributes

```sql
ATTRIBUTES > BALL
```

**Output:**
```
BALL ATTRIBUTES:
- COUNTRY
- HEALTH
- ATTACK
- REGIME
- RARITY
- EMOJI_ID
...
```

### Filter Nullable Fields

```sql
ATTRIBUTES > BALL > null
```

Shows only fields that can be NULL.

### Filter Required Fields

```sql
ATTRIBUTES > BALL > valid
```

Shows only required (non-nullable) fields.

### Using Alias

```sql
-- fields is alias for ATTRIBUTES
fields > BALL
```

## See Also

- [UPDATE](update.md) - Update attributes
- [VIEW](view.md) - View attribute values
- [CREATE](create.md) - Create instances
