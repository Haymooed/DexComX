# List Extensions

View all installed BallsDex extensions.

## Syntax

```
/dexadmin extension list
```

## Examples

### List Installed Extensions

```
/dexadmin extension list
```

## Output

### With Packages Installed

```
📦 Installed Extensions
Found 2 package(s)

`ballsdex_merchant_package`
Status: ✅ Enabled
URL: https://github.com/Haymooed/BallsDex-Merchant-Package.git

`ballsdex_art_package`
Status: ✅ Enabled
URL: https://github.com/Caylies/Art-BD-Package.git
```

### No Packages

```
📦 No extensions installed.
Use `/dexadmin extension add <url>` to install one.
```

## Information Shown

- Package name (path)
- Status (enabled/disabled)
- Git repository URL

## See Also

- [Add Extension](add.md) - Install new packages
- [Remove Extension](remove.md) - Uninstall packages
- [Update Extension](update.md) - Update packages
