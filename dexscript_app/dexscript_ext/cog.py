import traceback
import subprocess
import sys
from typing import TYPE_CHECKING

import discord
from ballsdex.settings import settings
from discord.ext import commands

from .parser import DexScriptParser
from .utils import Utils, config
from .extension_manager import ExtensionManager

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot

__version__ = "1.0"


class DexScript(commands.Cog):
    """
    DexComX commands
    """

    def __init__(self, bot: "BallsDexBot"):
        self.bot = bot
        self.extension_manager = ExtensionManager(bot)

    @commands.command()
    @commands.is_owner()
    async def run(self, ctx: commands.Context, *, code: str):
        """
        Executes DexComX code.

        Parameters
        ----------
        code: str
          The code you want to execute.
        """
        body = Utils.remove_code_markdown(code)

        dexscript_instance = DexScriptParser(ctx, self.bot)

        try:
            result = await dexscript_instance.execute(body)
        except Exception as error:
            full_error = traceback.format_exc() if config.debug else error
            await ctx.send(f"```ERROR: {full_error}```")
            return
        else:
            if result is not None:
                await ctx.send(f"```ERROR: {result}```")
                return

            await ctx.message.add_reaction("✅")

    @commands.group(name="dexadmin", invoke_without_command=True)
    @commands.is_owner()
    async def dexadmin(self, ctx: commands.Context):
        """
        DexComX admin commands.
        """
        await ctx.send_help(ctx.command)

    @dexadmin.command(name="extension")
    @commands.is_owner()
    async def extension(self, ctx: commands.Context, action: str, url: str = None):
        """
        Manage BallsDex extensions.

        Parameters
        ----------
        action: str
          Action to perform: add, remove, list, update
        url: str
          Git URL for the extension (required for add)
        
        Examples
        --------
        /dexadmin extension add https://github.com/User/Package.git
        /dexadmin extension remove package_name
        /dexadmin extension list
        /dexadmin extension update package_name
        """
        action = action.lower()

        if action == "add":
            if not url:
                await ctx.send("❌ URL is required for adding extensions.\n"
                              "Usage: `m.dexadmin extension add <git_url>`")
                return
            
            await self.extension_manager.add_extension(ctx, url)

        elif action == "remove":
            if not url:
                await ctx.send("❌ Package name is required for removing extensions.\n"
                              "Usage: `m.dexadmin extension remove <package_name>`")
                return
            
            await self.extension_manager.remove_extension(ctx, url)

        elif action == "list":
            await self.extension_manager.list_extensions(ctx)

        elif action == "update":
            if not url:
                await ctx.send("❌ Package name is required for updating extensions.\n"
                              "Usage: `m.dexadmin extension update <package_name>`")
                return
            
            await self.extension_manager.update_extension(ctx, url)

        else:
            await ctx.send(f"❌ Unknown action: `{action}`\n"
                          "Valid actions: `add`, `remove`, `list`, `update`")

    @commands.command()
    @commands.is_owner()
    async def about(self, ctx: commands.Context):
        """
        Displays information about DexComX.
        """
        embed = discord.Embed(
            title="DexComX",
            description=(
                "DexComX is a script-driven admin toolkit for BallsDex.\n\n"
                "**Original Creator:** [Cayla (DexScript)](https://github.com/Caylies/DexScript)\n"
                "**Current Maintainer:** haymooed\n\n"
                "📖 [Full Documentation](https://haymooed.github.io/DexComX/)\n"
                "💻 [GitHub Repository](https://github.com/Haymooed/DexComX)"
            ),
            color=discord.Color.from_str("#03BAFC"),
        )

        embed.add_field(
            name="Features",
            value=(
                "• Speed aliases (`set`, `show`, `rm`, `ls`)\n"
                "• Bulk filter operations\n"
                "• Eval presets & file management\n"
                "• Extension package manager"
            ),
            inline=False
        )

        embed.set_footer(text=f"DexComX v{__version__}")

        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def setting(self, ctx: commands.Context, setting: str, value: str | None = None):
        """
        Changes a DexComX setting.

        Parameters
        ----------
        setting: str
          The setting you want to toggle.
        value: str | None
          The value you want to set. For booleans, leave empty to toggle.
        """
        setting = setting.lower()

        if setting not in vars(config):
            await ctx.send(f"`{setting}` is not a valid setting.")
            return

        setting_value = vars(config)[setting]
        new_value = value

        if isinstance(setting_value, bool):
            new_value = bool(value) if value else not setting_value

        setattr(config, setting, new_value)

        await ctx.send(f"`{setting}` has been set to `{new_value}`")
