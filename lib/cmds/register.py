from lib.cmd_dispatch import CommandDispatcher
from lib.cmds.impl.register_credential import RegisterCredentialCommand


commands = [
    RegisterCredentialCommand()
]


def register_commands(dispatcher: CommandDispatcher):
    for cmd in commands:
        dispatcher.add_command(cmd)

