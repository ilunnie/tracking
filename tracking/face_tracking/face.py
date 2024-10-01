from .partials import *

from ..landmarks import Landmarks

class Face(InfosMethods):

    def __init__(self, landmarks: Landmarks) -> None:
        super().__init__(landmarks)