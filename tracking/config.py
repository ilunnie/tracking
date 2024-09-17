from typing import Tuple

from .exceptions import IncorrectInstanceException

class Config:
    def __init__(self):
        self._screen_width = 0
        self._screen_height = 0

    @property
    def SCREEN_SHAPE(self) -> Tuple[int, int]:
        return (self._screen_width, self._screen_height)
    
    @property
    def SCREEN_WIDTH(self) -> int:
        return self._screen_width
    
    @SCREEN_WIDTH.setter
    def SCREEN_WIDTH(self, value: int):
        if not isinstance(value, int):
            raise IncorrectInstanceException(type(value), int)
        self._screen_width = value

    @property
    def SCREEN_HEIGHT(self) -> int:
        return self._screen_height
    
    @SCREEN_HEIGHT.setter
    def SCREEN_HEIGHT(self, value: int):
        if not isinstance(value, int):
            raise IncorrectInstanceException(type(value), int)
        self._screen_height = value