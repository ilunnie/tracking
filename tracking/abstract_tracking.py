import mediapipe as mp

from abc import ABC, abstractmethod
from datetime import datetime
from mediapipe.tasks.python.vision.core.base_vision_task_api import BaseVisionTaskApi
from threading import Event
from typing import Callable, Optional

from .enums import RunningModeEnum

class AbstractTracking(ABC):
    def __init__(self, 
                 mesh: BaseVisionTaskApi,
                 result_callback: Optional[
                     Callable[
                         [list, mp.Image, int], 
                         None]] = None) -> None:
        self.mesh = mesh
        self.__running_mode = mesh._running_mode
        self.__result_callback = result_callback
        self.__callback = Event()
        
        self.__timestamp: int = 0
        self.__lastupdate: datetime = None
        
    @abstractmethod
    def callback(self, result, *args, **kwargs):
        self.__result = result
        self.__callback.set()
        if self.__result_callback:
            self.__result_callback(*args)
          
    @abstractmethod  
    def predict(self, *args, **kwargs):
        pass
        
    def detect(self, image: mp.Image) -> any:
        self.__callback.clear()
        if self.__running_mode == RunningModeEnum.LIVE_STREAM:
            now = datetime.now()
            if self.__lastupdate:
                self.__timestamp += int((now - self.__lastupdate).total_seconds() * 1000)
                self.__lastupdate = now
            else:
                self.__timestamp = 0
                self.__lastupdate = now
            self.mesh.detect_async(image, self.__timestamp)
        else:
            if self.__running_mode == RunningModeEnum.IMAGE:
                result = self.mesh.detect(image)
            else:
                self.__timestamp += 1
                result = self.mesh.detect_for_video(image, self.__timestamp)
            self.callback(result, image, self.__timestamp)

        self.__callback.wait()
        return self.__result