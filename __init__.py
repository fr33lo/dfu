"""
Discord File Updater

A tool to automatically update local files from Discord channels.
"""

# Version of the discord-file-updater package
__version__ = "0.2.0"

# Import main classes/functions to make them easily accessible
from .discord_file_updater import DiscordFileUpdater, main

# Define what should be imported with "from discord_file_updater import *"
__all__ = ['DiscordFileUpdater', 'main']