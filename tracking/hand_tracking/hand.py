from . import partials

from .abstract import HandAbstract

from ..enums.side import SideEnum
from ..landmarks import Landmarks

class Hand(*[getattr(partials, name)
             for name in dir(partials)
             if name.endswith('Methods')], HandAbstract):
    
    def __init__(self, side: SideEnum, landmarks: Landmarks) -> None:
        super().__init__(side, landmarks)