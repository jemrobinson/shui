from _typeshed import Incomplete

from .io_mixin import IOMixin as IOMixin

class ConsoleIO(IOMixin, Incomplete):
    def __init__(self, *args, **kwargs) -> None: ...
