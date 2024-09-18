import numpy as np

from numbers import Number
from typing import List, Tuple

from .utils.drawing import normalize_pixel

class Landmarks:
    def __init__(self, image: np.ndarray, landmarks: list):
        self.__image = image
        self.__landmarks = landmarks

    @property
    def image(self) -> np.ndarray:
        return self.__image

    def get_points(self, indexes: List[int]) -> List[Tuple[Number, Number, Number]]:
        '''
        Returns:
        3D coordinades list
        '''
        return [
            (point.x, point.y, point.z)
            for point
            in [self.__landmarks[idx] for idx in indexes]]
    
    def get_pixels(self, indexes: List[int]) -> List[Tuple[Number, Number]]:
        '''
        Returns:
        2D coordinades list
        '''
        height, width = self.__image.shape[:2]
        return [
            normalize_pixel(point.x, point.y, width, height)
            for point
            in [self.__landmarks[idx] for idx in indexes]]