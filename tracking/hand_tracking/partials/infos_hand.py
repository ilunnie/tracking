import numpy as np

from ..abstract import HandAbstract

from ...enums import FingerEnum
from ...utils import math

class InfosMethods(HandAbstract):
    def finger_is_raised(self, finger: FingerEnum, threshold: float = 0.7) -> bool:
        size = self.finger_size(finger)
        finger_tip = self.landmarks.get_points([FingerEnum.get_tip(finger)])[0]
        
        if finger == FingerEnum.THUMB:
            center_palm = self.center_palm()
            distance = math.euclidean_distance(finger_tip, center_palm)
            return size * threshold < distance
        
        bottom_palm_idx = self.indexes.HAND_PALM.value[0]
        sides_palm_idx = [(b if a == bottom_palm_idx else a) 
                          for a, b 
                          in self.indexes.HAND_PALM_CONNECTIONS.value
                          if bottom_palm_idx in (a, b)]
        
        bottom_palm, left_palm, right_palm = self.landmarks.get_points([bottom_palm_idx, *sides_palm_idx[-2:]])
        
        left_palm = math.center([bottom_palm, left_palm])
        right_palm = math.center([bottom_palm, right_palm])
        
        AP = np.array(finger_tip) - np.array(left_palm)
        AB = np.array(right_palm) - np.array(left_palm)
        
        cross_product = np.cross(AP, AB)
        
        distance = np.linalg.norm(cross_product) / np.linalg.norm(AB)
        
        return size * threshold < distance