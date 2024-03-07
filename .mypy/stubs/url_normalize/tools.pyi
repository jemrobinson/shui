from typing import NamedTuple

from _typeshed import Incomplete

class URL(NamedTuple):
    scheme: Incomplete
    userinfo: Incomplete
    host: Incomplete
    port: Incomplete
    path: Incomplete
    query: Incomplete
    fragment: Incomplete

def deconstruct_url(url): ...
def reconstruct_url(url): ...
def force_unicode(string, charset: str = ...): ...
def unquote(string, charset: str = ...): ...
def quote(string, safe: str = ...): ...
