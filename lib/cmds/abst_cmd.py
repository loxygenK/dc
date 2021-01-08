from abc import ABCMeta, abstractmethod
from lib.cmds.cmd_info import CommandInfo
from lib.config.config import Configuration
from typing import List

class AbstractCommand(metaclass=ABCMeta):
    @abstractmethod
    def get_command_info(self) -> CommandInfo:
        pass

    @abstractmethod
    def execute(self, argument: List[str], config: Configuration) -> bool:
        pass

