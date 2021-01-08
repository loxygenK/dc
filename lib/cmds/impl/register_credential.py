from lib.cmds.abst_cmd import AbstractCommand
from lib.cmds.cmd_info import CommandInfo

class RegisterCredentialCommand(AbstractCommand):
    def get_command_info(self) -> CommandInfo:
        return CommandInfo(
            "register",
            [],
            "Register the credentials for logging in to Discord."
        )

    def execute(self, args, config):
        print("")
