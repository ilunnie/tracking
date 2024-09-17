import numpy as np
import cv2

from typing import Tuple, Union

from .exceptions import IncorrectInstanceException

class WebCam:
    def __init__(self, video_capture: Union[cv2.VideoCapture, int] = 0):
        self.__video_capture = (video_capture 
                               if isinstance(video_capture, cv2.VideoCapture) 
                               else cv2.VideoCapture(video_capture))
        self.__frame = None
        self.__width = 0
        self.__height = 0

    def read(self) -> Tuple[bool, np.ndarray]:
        sucess, frame = self.__video_capture.read()
        if sucess:
            self.frame = frame
            return sucess, frame
        return sucess, self.__frame
    
    @property
    def shape(self) -> Tuple[int, int]:
        return (self.__width, self.__height)
    
    @property
    def width(self) -> int:
        return self.__width
    
    @property
    def height(self) -> int:
        return self.__height
    
    @property
    def frame(self) -> np.ndarray:
        return self.__frame
    
    @frame.setter
    def frame(self, value: np.ndarray):
        if not isinstance(value, np.ndarray):
            raise IncorrectInstanceException(type(value), np.ndarray)
        self.__height, self.__width = value.shape[:2]
        self.__frame = value

    @property
    def isOpened(self) -> bool:
        return self.__video_capture.isOpened()
    
    def close(self):
        self.__video_capture.release()