import sys
from lib.cmd_dispatch import CommandDispatcher
from lib.cmds.register import register_commands
from lib.config.config import Configuration


def main():
    cmd_dispatcher = CommandDispatcher()
    register_commands(cmd_dispatcher)

    if len(sys.argv) < 2:
        cmd_dispatcher.show_help()
        return

    config = Configuration()
    cmd_dispatcher.dispatch_command(sys.argv[:1], config)


if __name__ == "__main__":
    main()
