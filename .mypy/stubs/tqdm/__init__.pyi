from .std import TqdmDeprecationWarning as TqdmDeprecationWarning
from .std import TqdmExperimentalWarning as TqdmExperimentalWarning
from .std import TqdmKeyError as TqdmKeyError
from .std import TqdmMonitorWarning as TqdmMonitorWarning
from .std import TqdmTypeError as TqdmTypeError
from .std import TqdmWarning as TqdmWarning
from .std import tqdm as tqdm
from .std import trange as trange

def tqdm_notebook(*args, **kwargs): ...
def tnrange(*args, **kwargs): ...
