from .std import (
    TqdmDeprecationWarning as TqdmDeprecationWarning,
    TqdmExperimentalWarning as TqdmExperimentalWarning,
    TqdmKeyError as TqdmKeyError,
    TqdmMonitorWarning as TqdmMonitorWarning,
    TqdmTypeError as TqdmTypeError,
    TqdmWarning as TqdmWarning,
    tqdm as tqdm,
    trange as trange,
)

def tqdm_notebook(*args, **kwargs): ...
def tnrange(*args, **kwargs): ...
