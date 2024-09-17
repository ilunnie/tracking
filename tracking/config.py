from typing import Optional, Tuple

from .exceptions import IncorrectInstanceException
from .webcam import WebCam

class Config:
    def __init__(self):
        self.__screen_width = 0
        self.__screen_height = 0
        self.__video_capture = None

    @property
    def SCREEN_SHAPE(self) -> Tuple[int, int]:
        return (self.__screen_width, self.__screen_height)
    
    @property
    def SCREEN_WIDTH(self) -> int:
        return self.__screen_width
    
    @SCREEN_WIDTH.setter
    def SCREEN_WIDTH(self, value: int):
        if not isinstance(value, int):
            raise IncorrectInstanceException(type(value), int)
        self.__screen_width = value

    @property
    def SCREEN_HEIGHT(self) -> int:
        return self.__screen_height
    
    @SCREEN_HEIGHT.setter
    def SCREEN_HEIGHT(self, value: int):
        if not isinstance(value, int):
            raise IncorrectInstanceException(type(value), int)
        self.__screen_height = value

    @property
    def VIDEO_CAPTURE(self) -> Optional[WebCam]:
        return self.__video_capture
    
    @VIDEO_CAPTURE.setter
    def VIDEO_CAPTURE(self, value: WebCam):
        if not isinstance(value, WebCam):
            raise IncorrectInstanceException(type(value), WebCam)
        self.__video_capture = value