import numpy as np

from abc import ABC, abstractmethod

from .constants import FaceIndexes

from ..landmarks import Landmarks

class FaceAbstract(ABC):
    def __init__(self, landmarks: Landmarks) -> None:
        self.__landmarks = landmarks
        self.indexes = FaceIndexes

    @property
    def landmarks(self) -> Landmarks:
        return self.__landmarks
    
    @abstractmethod
    def direction(self):
        pass
    
    @abstractmethod
    def draw(self, image: np.ndarray, *args, **kwargs):
        pass
    
    @abstractmethod
    def draw_contour(self, image: np.ndarray, *args, **kwargs):
        pass