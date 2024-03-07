from typing import NamedTuple

from _typeshed import Incomplete

class _argument(NamedTuple):
    name: Incomplete
    flags: Incomplete
    description: Incomplete
    default: Incomplete

class _option(NamedTuple):
    long_name: Incomplete
    short_name: Incomplete
    flags: Incomplete
    description: Incomplete
    default: Incomplete

class Parser:
    @classmethod
    def parse(cls, expression): ...
