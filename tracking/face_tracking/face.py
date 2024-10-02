from .partials import *

from ..landmarks import Landmarks

class Face(InfosMethods, DrawingMethods):

    def __init__(self, landmarks: Landmarks) -> None:
        super().__init__(landmarks)