from .partials import *

from ..enums.side import SideEnum
from ..landmarks import Landmarks

class Hand(DrawingMethods, InfosMethods, MeasuresMethods):

    def __init__(self, side: SideEnum, landmarks: Landmarks) -> None:
        super().__init__(side, landmarks)