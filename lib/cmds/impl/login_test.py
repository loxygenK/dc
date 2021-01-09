from typing import List, Optional

import discord

from lib.cmds.abst_cmd import AbstractCommand
from lib.cmds.cmd_info import CommandInfo
from lib.config.config import Configuration
from lib.discord.client import DiscordClient
from lib.util.colored_print import success, log


class DiscordLoginTestCommand(AbstractCommand):
    def get_command_info(self) -> CommandInfo:
        return CommandInfo(
            "test-connect",
            [],
            "Try connecting to the Discord server, and show some information about you",
            discord=True
        )
        pass

    def execute(self, argument: List[str], config: Configuration, discord_session: Optional[DiscordClient] = None) -> bool:
        log("Connecting to Discord...")
        discord_session.access()
        success(f"Logged in as \"{discord_session.user.name}#{discord_session.user.discriminator}\"")
        print()
        print("Guild information:")
        for guild in discord_session.guilds:
            g: discord.Guild
            member = guild.get_member(discord_session.user.id)
            print(f"  {guild.name}")
            print(f"     Nick: {member.nick if member.nick is not None else '(not set)'}")
            print(f"     Channels: ")
            for category in guild.categories:
                print(f"     --- [{category.name}] ---------------------------")
                for channel in category.channels:
                    if type(channel) is discord.TextChannel:
                        flag = "[NSFW] " if channel.nsfw else "       "
                    else:
                        flag = "[ VC ] "
                    print(f"          {flag}{channel.name}")
