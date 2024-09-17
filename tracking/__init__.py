from typing import Union, Tuple, List

from . import exceptions

from .constants import CONFIG
from .enums import TypeEnum as type

def init(
        screen_size: Union[Tuple[int, int], List[int]],
        flags: List[Union[int, type]] = 0
):
    CONFIG.SCREEN_WIDTH, CONFIG.SCREEN_HEIGHT = screen_size
    
    for flag in [flags] if isinstance(flags, (int, type)) else set(flags):
        value = flag.value if isinstance(flag, type) else flag
        
        if value == 0:
            pass
        elif value == 1:
            pass
        elif value == 2:
            pass
        else:
            raise exceptions.InvalidFlagException(f"Invalid Flag {flag}, use a tracking.type value")