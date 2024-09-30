from ..abstract import FaceAbstract

from ...utils import math

class InfosMethods(FaceAbstract):
    def direction(self):
        left_point, center_point, right_point = self.landmarks.get_points([356, 9, 127])

        center = math.center([left_point, right_point])
        return math.direction(center, center_point)