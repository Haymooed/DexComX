# Extension Manager

DexComX includes a built-in extension manager that lets you install, update, and remove BallsDex packages directly from Discord.

## What is the Extension Manager?

The extension manager allows you to:

- Install packages from GitHub repositories
- Manage installed packages without editing config files
- Update packages to their latest versions
- Remove packages cleanly

## Why Use It?

**Before:**
```toml
# Manually edit config/extra.toml
[[ballsdex.packages]]
location = "git+https://github.com/User/Package.git"
path = "package_name"
enabled = true
editable = false
```

**Now:**
```
/dexadmin extension add https://github.com/User/Package.git
```

## Available Commands

All extension manager commands are under the `/dexadmin extension` group:

- **[add](add.md)** - Install a new extension
- **[remove](remove.md)** - Remove an installed extension
- **[list](list.md)** - Show all installed extensions
- **[update](update.md)** - Update an extension to latest version

## Quick Example

### Install a Package

```
/dexadmin extension add https://github.com/Haymooed/BallsDex-Merchant-Package.git
```

DexComX will:

1. Download the package via pip
2. Add it to `config/extra.toml`
3. Attempt to load the extension
4. Show success or error message

### List Installed Packages

```
/dexadmin extension list
```

Shows all packages with their URLs and status.

### Update a Package

```
/dexadmin extension update ballsdex_merchant_package
```

Pulls the latest version and reinstalls.

### Remove a Package

```
b.dexadmin extension remove ballsdex_merchant_package
```

Removes from config and unloads the extension.

## How It Works

### Installation Flow

1. User runs `/dexadmin extension add <url>`
2. DexComX validates the git URL
3. Package is downloaded via `pip install git+<url>`
4. Entry is added to `config/extra.toml`
5. Extension is loaded (if possible)
6. Success/failure message is shown

### Configuration

All changes are saved to `config/extra.toml` in the standard BallsDex format:

```toml
[[ballsdex.packages]]
location = "git+https://github.com/User/Package.git"
path = "package_name"
enabled = true
editable = false
```

## Requirements

- Bot owner permissions (all `/dexadmin` commands are owner-only)
- Git-based package URLs (GitHub, GitLab, etc.)
- Package must follow BallsDex package structure

## Limitations

- Some packages may require a bot restart to fully activate
- Only works with git URLs (not local paths)
- Package names are auto-generated from URLs

## Best Practices

1. **Always list first** - Run `b.dexadmin extension list` before adding
2. **Test in development** - Try new packages on a test bot first
3. **Keep updated** - Regularly update packages with `b.dexadmin extension update`
4. **Remove unused** - Clean up packages you're not using

## Troubleshooting

### Package won't load

Try restarting the bot. Some packages need a full restart to activate.

### "Package already installed"

Use `b.dexadmin extension list` to see what's installed, or use `update` instead of `add`.

### Permission errors

Ensure you're the bot owner. All `b.dexadmin` commands are owner-only.

## See Also

- [Add Extension](add.md) - Install packages
- [Remove Extension](remove.md) - Uninstall packages
- [List Extensions](list.md) - View installed packages
- [Update Extension](update.md) - Update to latest versions
