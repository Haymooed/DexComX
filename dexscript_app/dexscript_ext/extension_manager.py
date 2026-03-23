import os
import re
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING

import discord
import toml

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot
    from discord.ext.commands import Context


class ExtensionManager:
    """
    Manages BallsDex extension packages via git URLs.
    """

    def __init__(self, bot: "BallsDexBot"):
        self.bot = bot
        self.config_file = Path("config/extra.toml")
        self.packages_key = "ballsdex.packages"

    def _load_config(self) -> dict:
        """Load the extra.toml configuration file."""
        if not self.config_file.exists():
            return {self.packages_key: []}
        
        with open(self.config_file, "r") as f:
            config = toml.load(f)
        
        if self.packages_key not in config:
            config[self.packages_key] = []
        
        return config

    def _save_config(self, config: dict):
        """Save the configuration back to extra.toml."""
        self.config_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.config_file, "w") as f:
            toml.dump(config, f)

    def _extract_package_name(self, url: str) -> str:
        """Extract package name from git URL."""
        # Extract from URLs like: https://github.com/User/Package-Name.git
        match = re.search(r'/([^/]+?)(?:\.git)?$', url)
        if match:
            return match.group(1).replace("-", "_").replace(" ", "_").lower()
        return url.replace("/", "_").replace(".", "_").lower()

    async def add_extension(self, ctx: "Context", url: str):
        """
        Add a new extension from a git URL.
        
        Parameters
        ----------
        ctx: Context
            The command context
        url: str
            Git repository URL
        """
        # Validate URL format
        if not url.startswith("http") and not url.startswith("git@"):
            await ctx.send("❌ Invalid URL format. Use HTTPS or SSH git URLs.\n"
                          "Example: `https://github.com/User/Package.git`")
            return

        # Extract package name from URL
        package_name = self._extract_package_name(url)
        
        # Check if package already exists
        config = self._load_config()
        packages = config.get(self.packages_key, [])
        
        for pkg in packages:
            if pkg.get("location") == f"git+{url}":
                await ctx.send(f"⚠️ Package `{package_name}` is already installed from this URL.")
                return

        # Add new package entry
        new_package = {
            "location": f"git+{url}",
            "path": package_name,
            "enabled": True,
            "editable": False
        }
        
        packages.append(new_package)
        config[self.packages_key] = packages
        
        # Save configuration
        self._save_config(config)
        
        # Try to install the package
        embed = discord.Embed(
            title="📦 Installing Extension",
            description=f"Installing `{package_name}` from:\n```{url}```",
            color=discord.Color.blue()
        )
        msg = await ctx.send(embed=embed)
        
        try:
            # Install package using pip
            process = subprocess.run(
                [sys.executable, "-m", "pip", "install", f"git+{url}"],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if process.returncode == 0:
                # Try to load the extension
                try:
                    await self.bot.load_extension(f"{package_name}.{package_name}_ext")
                    
                    embed = discord.Embed(
                        title="✅ Extension Installed",
                        description=f"Successfully installed and loaded `{package_name}`",
                        color=discord.Color.green()
                    )
                    embed.add_field(name="URL", value=f"```{url}```", inline=False)
                    embed.add_field(name="Path", value=f"`{package_name}`", inline=True)
                    embed.set_footer(text="Extension is now active. Restart may be required for full functionality.")
                    
                except Exception as e:
                    embed = discord.Embed(
                        title="⚠️ Installed but Not Loaded",
                        description=f"Package installed but failed to load automatically.\n```{str(e)}```",
                        color=discord.Color.orange()
                    )
                    embed.add_field(name="Action Required", value="Restart the bot to activate this extension.", inline=False)
            else:
                embed = discord.Embed(
                    title="❌ Installation Failed",
                    description=f"```{process.stderr}```",
                    color=discord.Color.red()
                )
                # Remove from config since install failed
                packages.remove(new_package)
                config[self.packages_key] = packages
                self._save_config(config)
        
        except subprocess.TimeoutExpired:
            embed = discord.Embed(
                title="⏱️ Installation Timeout",
                description="Installation took too long. The package may still be installing in the background.",
                color=discord.Color.orange()
            )
        except Exception as e:
            embed = discord.Embed(
                title="❌ Installation Error",
                description=f"```{str(e)}```",
                color=discord.Color.red()
            )
        
        await msg.edit(embed=embed)

    async def remove_extension(self, ctx: "Context", package_name: str):
        """
        Remove an installed extension.
        
        Parameters
        ----------
        ctx: Context
            The command context
        package_name: str
            Name of the package to remove
        """
        config = self._load_config()
        packages = config.get(self.packages_key, [])
        
        # Find package
        package_to_remove = None
        for pkg in packages:
            if pkg.get("path") == package_name:
                package_to_remove = pkg
                break
        
        if not package_to_remove:
            await ctx.send(f"❌ Package `{package_name}` not found in configuration.\n"
                          "Use `/admin extension list` to see installed packages.")
            return
        
        # Remove from config
        packages.remove(package_to_remove)
        config[self.packages_key] = packages
        self._save_config(config)
        
        # Try to unload extension
        try:
            await self.bot.unload_extension(f"{package_name}.{package_name}_ext")
        except:
            pass  # Extension may not be loaded
        
        embed = discord.Embed(
            title="✅ Extension Removed",
            description=f"Removed `{package_name}` from configuration.",
            color=discord.Color.green()
        )
        embed.add_field(
            name="Note",
            value="The package files remain installed. Restart the bot to fully unload.",
            inline=False
        )
        
        await ctx.send(embed=embed)

    async def list_extensions(self, ctx: "Context"):
        """
        List all installed extensions.
        
        Parameters
        ----------
        ctx: Context
            The command context
        """
        config = self._load_config()
        packages = config.get(self.packages_key, [])
        
        if not packages:
            await ctx.send("📦 No extensions installed.\n"
                          "Use `/admin extension add <url>` to install one.")
            return
        
        embed = discord.Embed(
            title="📦 Installed Extensions",
            description=f"Found {len(packages)} package(s)",
            color=discord.Color.blue()
        )
        
        for pkg in packages:
            location = pkg.get("location", "Unknown")
            path = pkg.get("path", "Unknown")
            enabled = "✅ Enabled" if pkg.get("enabled", False) else "❌ Disabled"
            
            # Clean up git+ prefix for display
            display_location = location.replace("git+", "")
            
            embed.add_field(
                name=f"`{path}`",
                value=f"**Status:** {enabled}\n**URL:** {display_location}",
                inline=False
            )
        
        await ctx.send(embed=embed)

    async def update_extension(self, ctx: "Context", package_name: str):
        """
        Update an installed extension to latest version.
        
        Parameters
        ----------
        ctx: Context
            The command context
        package_name: str
            Name of the package to update
        """
        config = self._load_config()
        packages = config.get(self.packages_key, [])
        
        # Find package
        package_to_update = None
        for pkg in packages:
            if pkg.get("path") == package_name:
                package_to_update = pkg
                break
        
        if not package_to_update:
            await ctx.send(f"❌ Package `{package_name}` not found.\n"
                          "Use `/admin extension list` to see installed packages.")
            return
        
        location = package_to_update.get("location", "")
        
        embed = discord.Embed(
            title="🔄 Updating Extension",
            description=f"Updating `{package_name}`...",
            color=discord.Color.blue()
        )
        msg = await ctx.send(embed=embed)
        
        try:
            # Update using pip
            process = subprocess.run(
                [sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", location],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if process.returncode == 0:
                embed = discord.Embed(
                    title="✅ Extension Updated",
                    description=f"Successfully updated `{package_name}`",
                    color=discord.Color.green()
                )
                embed.add_field(
                    name="Action Required",
                    value="Restart the bot to apply updates.",
                    inline=False
                )
            else:
                embed = discord.Embed(
                    title="❌ Update Failed",
                    description=f"```{process.stderr}```",
                    color=discord.Color.red()
                )
        
        except subprocess.TimeoutExpired:
            embed = discord.Embed(
                title="⏱️ Update Timeout",
                description="Update took too long. Check logs for details.",
                color=discord.Color.orange()
            )
        except Exception as e:
            embed = discord.Embed(
                title="❌ Update Error",
                description=f"```{str(e)}```",
                color=discord.Color.red()
            )
        
        await msg.edit(embed=embed)