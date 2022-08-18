from _typeshed import Incomplete
from .commands import BaseCommand as BaseCommand
from typing import Optional, Tuple

class Application:
    def __init__(
        self,
        name: str = ...,
        version: str = ...,
        complete: bool = ...,
        config: Optional[Incomplete] = ...,
    ) -> None: ...
    def add_commands(self, *commands: Tuple[BaseCommand]) -> None: ...
    def add(self, command: BaseCommand) -> Application: ...
    def find(self, name: str) -> BaseCommand: ...
