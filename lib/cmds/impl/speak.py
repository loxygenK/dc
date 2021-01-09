import asyncio
from typing import List, Optional

from discord import TextChannel

from lib.cmds.abst_cmd import AbstractCommand
from lib.cmds.cmd_info import CommandInfo, Argument
from lib.config.config import Configuration
from lib.discord.client import DiscordClient
from lib.util.colored_print import log, fatal, success


class DiscordSpeakCommand(AbstractCommand):
    def get_command_info(self) -> CommandInfo:
        return CommandInfo(
            "say",
            [
                Argument("channel_name", "The name of channel you want to speak at.", False),
                Argument("content", "The content what you want to speak.", False)
            ],
            "Speak at the selected channel.",
            discord=True
        )

    def execute(self, argument: List[str], config: Configuration, discord: Optional[DiscordClient] = None) -> bool:
        log("Connecting to the Discord...")
        discord.access()
        chan = discord.search_channel(argument[0], [TextChannel])
        if chan is None:
            fatal("Channel not found! Use `test-connect` to list up available channels.")
            return False
        log(f"Speaking at {chan.guild.name}/{chan.name}")
        asyncio.get_event_loop().run_until_complete(chan.send(argument[1]))
        success("Done!")
        return True

