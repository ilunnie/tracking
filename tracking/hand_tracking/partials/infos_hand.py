from ..abstract import HandAbstract

from ...enums import FingerEnum
from ...utils import math

class InfosMethods(HandAbstract):
    def finger_is_raised(self, finger: FingerEnum, threshold: float = 0.7) -> bool:
        size = self.finger_size(finger)
        
        center_palm = self.center_palm()
        finger_tip = self.landmarks.get_points(FingerEnum.get_tip(finger))[0]
        
        distance = math.euclidean_distance(finger_tip, center_palm)
        
        return size * threshold < distance