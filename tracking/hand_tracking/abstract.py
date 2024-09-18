import numpy as np

from abc import ABC, abstractmethod

from .constants import HandIndexes

from ..enums import FingerEnum, SideEnum
from ..landmarks import Landmarks

class HandAbstract(ABC):
    def __init__(self, side: SideEnum, landmarks: Landmarks) -> None:
        self.__side = side
        self.__landmarks = landmarks
        
    @property
    def side(self) -> SideEnum:
        return self.__side
    
    @property
    def landmarks(self) -> Landmarks:
        return self.__landmarks
    
    @property
    def indexes(self) -> HandIndexes:
        return HandIndexes
    
    @abstractmethod
    def finger_size(self, finger: FingerEnum) -> float:
        pass
    
    @abstractmethod
    def center_palm(self) -> tuple:
        pass
    
    @abstractmethod
    def finger_is_raised(self, finger: FingerEnum, threshold: float = .7) -> bool:
        pass

    @abstractmethod
    def draw(self, image: np.ndarray, *args, **kwargs):
        pass