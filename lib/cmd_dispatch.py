from typing import List
from lib.cmds.abst_cmd import AbstractCommand
from lib.config.config import Configuration


class CommandDispatcher:

    def __init__(self):
        self.command: List[AbstractCommand] = []

    def add_command(self, cmd: AbstractCommand):
        self.command.append(cmd)

    def show_help(self):
        help_text = "--- DC / Discord CLI Client ---\n"
        help_text += "\n"
        for cmd in self.command:
            cmd_info = cmd.get_command_info()
            arg_text = " ".join(list(map(lambda x: str(x), cmd_info.arg)))
            help_text += (
                f"  {cmd_info.name} {arg_text}\n"
                f"     {cmd_info.description}\n"
            )

        print(help_text)

    def dispatch_command(self, args: List[str], config: Configuration):
        if args[0] == "help":
            self.show_help()
            return

        for cmd in self.command:
            info = cmd.get_command_info()
            if info.name != args[0]:
                continue

            essential_args = list(filter(lambda x: not x.option, info.arg))
            if not (len(essential_args) <= (len(args) - 1) <= len(info.arg)):
                print("[!] Invalid argument number.")
                print("    Check proper syntax for this command using help.")

            cmd.execute(args[1:], config)
            return

        print(f"[!] No such command: {args[0]}")

