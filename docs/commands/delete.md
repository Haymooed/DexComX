# DELETE

Deletes a model instance.

## Syntax

```
DELETE > MODEL > IDENTIFIER
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `MODEL` | Required | Model class: `BALL`, `REGIME`, `ECONOMY`, `SPECIAL` |
| `IDENTIFIER` | Required | Name/identifier of the instance to delete |

## Behavior

- Permanently removes the specified instance
- Cannot be undone
- Returns confirmation message

## Examples

### Delete a Ball

```sql
DELETE > BALL > Germany
```

**Output:**
```
Deleted `Germany` ball
```

### Delete Multiple Instances

```sql
DELETE > BALL > OldBall1
DELETE > BALL > OldBall2
DELETE > BALL > OldBall3
```

### Using Aliases

```sql
-- rm is alias for DELETE
rm > BALL > OldBall

-- del is also an alias
del > BALL > TestBall
```

## Safety Tips

!!! warning "Permanent Deletion"
    Deleted instances cannot be recovered. Always verify the identifier before deleting.

### Verify Before Deleting

```sql
-- Check the ball exists first
VIEW > BALL > OldBall

-- Then delete
DELETE > BALL > OldBall
```

## Bulk Deletion

For deleting multiple instances matching a condition, use `FILTER.DELETE`:

```sql
-- Delete all balls with Communist regime
FILTER.DELETE > BALL > REGIME > Communist
```

## Error Handling

If the instance doesn't exist:

```
ERROR: 'NonExistentBall' does not exist.
```

DexComX provides autocorrect suggestions if you mistype.

## See Also

- [CREATE](create.md) - Create new instances
- [FILTER.DELETE](filter-delete.md) - Bulk deletion
- [VIEW](view.md) - Verify instance before deleting
