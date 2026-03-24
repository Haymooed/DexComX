# CREATE

Creates a new model instance with default values for required fields.

## Syntax

```
CREATE > MODEL > IDENTIFIER
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `MODEL` | Required | Model class: `BALL`, `REGIME`, `ECONOMY`, `SPECIAL` |
| `IDENTIFIER` | Required | Name/identifier for the new instance |

## Behavior

- Creates a new instance of the specified model
- Auto-populates required fields with default values
- Returns confirmation message

## Examples

### Create a Ball

```sql
CREATE > BALL > Germany
```

**Output:**
```
Created `Germany` ball
```

### Create a Regime

```sql
CREATE > REGIME > Republic
```

### Create Multiple Instances

```sql
CREATE > BALL > Spain
CREATE > BALL > Italy
CREATE > BALL > Portugal
```

## After Creation

After creating an instance, you'll typically want to update its attributes:

```sql
CREATE > BALL > NewCountry
UPDATE > BALL > NewCountry > HEALTH > 100
UPDATE > BALL > NewCountry > ATTACK > 90
UPDATE > BALL > NewCountry > REGIME > Democracy
UPDATE > BALL > NewCountry > RARITY > 1.0
```

## Default Values

DexComX automatically sets safe defaults for required fields:

- **Numeric fields**: `1` (integers), `1.0` (floats)
- **Text fields**: `"placeholder"`
- **Boolean fields**: `False`
- **Foreign keys**: First available instance from related model
- **JSON fields**: `{}`

## Template Helper

For complex models like BALL, use the template helper:

```sql
TEMPLATE > CREATE > BALL > Germany
```

This generates a full setup template with all common fields.

## See Also

- [UPDATE](update.md) - Modify instance attributes
- [DELETE](delete.md) - Remove instances
- [VIEW](view.md) - Inspect instance data
- [TEMPLATE.CREATE](template-create.md) - Generate setup templates
