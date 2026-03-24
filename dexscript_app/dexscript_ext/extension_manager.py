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
        Show instructions for manually adding an extension.
        
        Parameters
        ----------
        ctx: Context
            The command context
        url: str
            Git repository URL
        """
        # Extract package name from URL
        package_name = self._extract_package_name(url)
        
        embed = discord.Embed(
            title="📦 Manual Installation Required",
            description=f"To install `{package_name}`, add this to your `config/extra.toml`:",
            color=discord.Color.blue()
        )
        
        config_block = f"""```toml
[[ballsdex.packages]]
location = "git+{url}"
path = "{package_name}"
enabled = true
editable = false
```"""
        
        embed.add_field(
            name="Step 1: Edit config/extra.toml",
            value=config_block,
            inline=False
        )
        
        embed.add_field(
            name="Step 2: Restart the bot",
            value="The extension will be installed automatically on restart.",
            inline=False
        )
        
        embed.set_footer(text="Config file is read-only in this environment")
        
        await ctx.send(embed=embed)

    async def remove_extension(self, ctx: "Context", package_name: str):
        """
        Show instructions for manually removing an extension.
        
        Parameters
        ----------
        ctx: Context
            The command context
        package_name: str
            Name of the package to remove
        """
        embed = discord.Embed(
            title="🗑️ Manual Removal Required",
            description=f"To remove `{package_name}`:",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="Step 1: Edit config/extra.toml",
            value=f"Remove the `[[ballsdex.packages]]` block for `{package_name}`",
            inline=False
        )
        
        embed.add_field(
            name="Step 2: Restart the bot",
            value="The extension will be unloaded on restart.",
            inline=False
        )
        
        embed.set_footer(text="Config file is read-only in this environment")
        
        await ctx.send(embed=embed)

    async def list_extensions(self, ctx: "Context"):
        """
        List all installed extensions from config file.
        
        Parameters
        ----------
        ctx: Context
            The command context
        """
        try:
            config = self._load_config()
            packages = config.get(self.packages_key, [])
        except Exception as e:
            await ctx.send(f"❌ Could not read config file: {str(e)}")
            return
        
        if not packages:
            await ctx.send("📦 No extensions installed.\n"
                          "Add extensions manually to `config/extra.toml`")
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
        Show instructions for manually updating an extension.
        
        Parameters
        ----------
        ctx: Context
            The command context
        package_name: str
            Name of the package to update
        """
        embed = discord.Embed(
            title="🔄 Manual Update Required",
            description=f"To update `{package_name}`:",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="Method 1: Restart with editable=true",
            value="Set `editable = true` in config/extra.toml for auto-updates on restart.",
            inline=False
        )
        
        embed.add_field(
            name="Method 2: Manual pip update",
            value=f"Run: `pip install --upgrade --force-reinstall git+<url>`",
            inline=False
        )
        
        embed.add_field(
            name="Then restart the bot",
            value="Changes will apply after restart.",
            inline=False
        )
        
        embed.set_footer(text="Config file is read-only in this environment")
        
        await ctx.send(embed=embed)
