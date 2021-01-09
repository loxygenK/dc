from abc import ABCMeta, abstractmethod
from lib.cmds.cmd_info import CommandInfo
from lib.config.config import Configuration
from typing import List, Optional

from lib.discord.client import DiscordClient


class AbstractCommand(metaclass=ABCMeta):
    @abstractmethod
    def get_command_info(self) -> CommandInfo:
        pass

    @abstractmethod
    def execute(self, argument: List[str], config: Configuration, discord: Optional[DiscordClient] = None) -> bool:
        pass

