from dataclasses import dataclass
from typing import List


@dataclass
class Argument:
    name: str
    description: str
    option: bool

    def __str__(self):
        name_text = (
            ("[" if self.option else "") +
            self.name +
            ("]" if self.option else "")
        )
        return name_text


@dataclass
class CommandInfo:
    name: str
    arg: List[Argument]
    description: str
    discord: bool = False

