# Add Extension

Install a new BallsDex package from a git repository.

## Syntax

```
/admin extension add <url>
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `url` | Required | Git repository URL (HTTPS or SSH) |

## Behavior

1. Validates the git URL
2. Extracts package name from URL
3. Downloads package via pip
4. Adds entry to `config/extra.toml`
5. Attempts to load the extension
6. Shows installation status

## Examples

### Install from GitHub (HTTPS)

```
/admin extension add https://github.com/Haymooed/BallsDex-Merchant-Package.git
```

### Install from GitHub (SSH)

```
/admin extension add git@github.com:User/Package.git
```

### Install from GitLab

```
/admin extension add https://gitlab.com/user/package.git
```

## Output

### Successful Installation

```
📦 Installing Extension
Installing `ballsdex_merchant_package` from:
https://github.com/Haymooed/BallsDex-Merchant-Package.git

✅ Extension Installed
Successfully installed and loaded `ballsdex_merchant_package`

URL: https://github.com/Haymooed/BallsDex-Merchant-Package.git
Path: ballsdex_merchant_package

Extension is now active. Restart may be required for full functionality.
```

### Already Installed

```
⚠️ Package `ballsdex_merchant_package` is already installed from this URL.
```

### Installation Failed

```
❌ Installation Failed
[error details]
```

## What Gets Added to Config

The command automatically adds to `config/extra.toml`:

```toml
[[ballsdex.packages]]
location = "git+https://github.com/Haymooed/BallsDex-Merchant-Package.git"
path = "ballsdex_merchant_package"
enabled = true
editable = false
```

## Package Naming

Package names are auto-generated from the URL:

- `https://github.com/User/My-Package.git` → `my_package`
- Hyphens and spaces become underscores
- Converted to lowercase

## After Installation

### Check if Loaded

```
/admin extension list
```

Should show your new package with status `✅ Enabled`.

### If Not Working

Some packages require a full bot restart:

1. Stop the bot
2. Restart the bot
3. Extension should now be active

## Troubleshooting

### Invalid URL Format

```
❌ Invalid URL format. Use HTTPS or SSH git URLs.
Example: `https://github.com/User/Package.git`
```

**Solution:** Ensure you're using a valid git URL starting with `http` or `git@`.

### Installation Timeout

```
⏱️ Installation Timeout
Installation took too long. The package may still be installing in the background.
```

**Solution:** Wait a few minutes and check `/admin extension list`.

### Permission Errors

```
❌ Installation Error
[Permission denied]
```

**Solution:** Ensure the bot process has write access to the config directory.

## Best Practices

1. **Check before installing** - Run `/admin extension list` first
2. **Test on development bot** - Try new packages in a test environment
3. **Read package docs** - Check the package's README for special requirements
4. **Monitor logs** - Watch bot logs during installation for errors

## See Also

- [Remove Extension](remove.md) - Uninstall packages
- [List Extensions](list.md) - View installed packages
- [Update Extension](update.md) - Update to latest version