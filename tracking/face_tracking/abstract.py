from abc import ABC, abstractmethod

from ..landmarks import Landmarks

class FaceAbstract(ABC):
    def __init__(self, landmarks: Landmarks) -> None:
        self.__landmarks = landmarks

    @property
    def landmarks(self) -> Landmarks:
        return self.__landmarks
    
    @abstractmethod
    def direction(self):
        pass