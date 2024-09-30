from ..abstract import HandAbstract

from ...enums import FingerEnum
from ...utils import math

class MeasuresMethods(HandAbstract):
    def finger_size(self, finger: FingerEnum) -> float:
        points = FingerEnum.get_points(finger)
        points = self.landmarks.get_points(points)
        
        sizes = [
            math.euclidean_distance(points[i], points[i + 1])
            for i in range(len(points) - 1)]
        return sum(sizes)
    
    def center_palm(self) -> tuple:
        indexes = self.indexes.HAND_PALM.value
        points = self.landmarks.get_points(indexes)
        return math.center(points)