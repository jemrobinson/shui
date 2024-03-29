from _typeshed import Incomplete

CUR_OS: Incomplete
IS_WIN: Incomplete
IS_NIX: Incomplete
RE_ANSI: Incomplete

class FormatReplace:
    replace: Incomplete
    format_called: int
    def __init__(self, replace: str = ...) -> None: ...
    def __format__(self, _): ...

class Comparable:
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class ObjectWrapper:
    def __getattr__(self, name): ...
    def __setattr__(self, name, value): ...
    def wrapper_getattr(self, name): ...
    def wrapper_setattr(self, name, value): ...
    def __init__(self, wrapped) -> None: ...

class SimpleTextIOWrapper(ObjectWrapper):
    def __init__(self, wrapped, encoding) -> None: ...
    def write(self, s): ...
    def __eq__(self, other): ...

class DisableOnWriteError(ObjectWrapper):
    @staticmethod
    def disable_on_exception(tqdm_instance, func): ...
    def __init__(self, wrapped, tqdm_instance) -> None: ...
    def __eq__(self, other): ...

class CallbackIOWrapper(ObjectWrapper):
    def __init__(self, callback, stream, method: str = ...): ...

def disp_len(data): ...
def disp_trim(data, length): ...
