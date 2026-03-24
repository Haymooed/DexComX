# Update Extension

Update an installed extension to the latest version.

## Syntax

```
m.dexadmin extension update <package_name>
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `package_name` | Required | Name of the package to update |

## Behavior

1. Pulls latest version from git repository
2. Reinstalls using pip with `--force-reinstall`
3. Shows update status

## Examples

### Update a Package

```
m.dexadmin extension update ballsdex_merchant_package
```

## Output

### Successful Update

```
✅ Extension Updated
Successfully updated `ballsdex_merchant_package`

Action Required:
Restart the bot to apply updates.
```

### Package Not Found

```
❌ Package `unknown_package` not found.
Use `m.dexadmin extension list` to see installed packages.
```

### Update Failed

```
❌ Update Failed
[error details]
```

## Notes

- Always restart bot after updating
- Updates pull from the same URL used during installation
- Use `m.dexadmin extension list` to find package names

## Best Practices

1. **Check for updates regularly** - Keep packages up to date
2. **Test in development first** - Try updates on test bot
3. **Restart after updating** - Required for changes to take effect

## See Also

- [Add Extension](add.md) - Install packages
- [Remove Extension](remove.md) - Uninstall packages
- [List Extensions](list.md) - View installed packages
