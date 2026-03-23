# Remove Extension

Remove an installed BallsDex package.

## Syntax

```
/admin extension remove <package_name>
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `package_name` | Required | Name of the installed package |

## Behavior

1. Removes package from `config/extra.toml`
2. Attempts to unload the extension
3. Shows confirmation message

## Examples

### Remove a Package

```
/admin extension remove ballsdex_merchant_package
```

## Output

### Successful Removal

```
✅ Extension Removed
Removed `ballsdex_merchant_package` from configuration.

Note:
The package files remain installed. Restart the bot to fully unload.
```

### Package Not Found

```
❌ Package `unknown_package` not found in configuration.
Use `/admin extension list` to see installed packages.
```

## Notes

- Package files remain in Python environment
- Restart bot to fully unload extension
- Use `/admin extension list` to find exact package names

## See Also

- [Add Extension](add.md) - Install packages
- [List Extensions](list.md) - View installed packages
- [Update Extension](update.md) - Update packages
