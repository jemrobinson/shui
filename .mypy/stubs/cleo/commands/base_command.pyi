from typing import Optional

from _typeshed import Incomplete

class CommandError(Exception): ...

class BaseCommand:
    name: Incomplete
    description: Incomplete
    help: Incomplete
    arguments: Incomplete
    options: Incomplete
    aliases: Incomplete
    enabled: bool
    hidden: bool
    commands: Incomplete
    def __init__(self) -> None: ...
    @property
    def config(self) -> Incomplete: ...
    @property
    def application(self): ...
    def handle(
        self,
        args: Optional[Incomplete],
        io: Optional[Incomplete],
        command: Optional[Incomplete],
    ) -> Optional[int]: ...
    def set_application(self, application) -> None: ...
    def add_sub_command(self, command: BaseCommand) -> None: ...
    def default(self, default: bool = ...) -> BaseCommand: ...
    def anonymous(self) -> BaseCommand: ...
