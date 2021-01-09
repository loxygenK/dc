from lib.cmds.abst_cmd import AbstractCommand
from lib.cmds.cmd_info import CommandInfo
from lib.config.config import Configuration

from lib.util.colored_print import question, success

import colored as col

class RegisterCredentialCommand(AbstractCommand):
    def get_command_info(self) -> CommandInfo:
        return CommandInfo(
            "register",
            [],
            "Register the credentials for logging in to Discord."
        )

    def execute(self, argument, config: Configuration, discord=None):
        if config.discord_token != "":
            intension = question(
                "Seems you already registered the token to login Discord.\n"
                "Do you want to delete current token, and register new one? [yes/other]"
            )
            if intension != "yes":
                print("Aborted.")
                return
            print()

        print("Please provide your Discord Bot Token.")
        print("--> https://discord.com/developers/applications")
        print()
        print("For the detailed informations, read 'README.md'.")
        print()
        token = question("What was the token to login Discord?", override=True)

        config.discord_token = token
        config.save_config()

        success("Updated configuration!")

