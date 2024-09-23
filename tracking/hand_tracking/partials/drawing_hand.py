import cv2
import numpy as np

from typing import List, Tuple

from ..abstract import HandAbstract

from ...enums import FingerEnum
from ...utils import normalize_pixel

class DrawingHand(HandAbstract):
    def draw(self,
             image: np.ndarray,
             color: Tuple[int, int, int],
             point_scale:Tuple[int, int] = (5, 50),
             connections: bool = True,
             thickness: int = 2,
             inplace: bool = True,
             palm: bool = True,
             fingers: List[FingerEnum] = [
                 FingerEnum.THUMB,
                 FingerEnum.INDEX,
                 FingerEnum.MIDDLE,
                 FingerEnum.RING,
                 FingerEnum.PINKY]):
        indexes = set()
        if palm:
            indexes = indexes.union(self.indexes[f"HAND_PALM{'_CONNECTIONS' if connections else ''}"].value)
        for f in fingers:
            name = f.name if f == FingerEnum.THUMB else f.name + "_FINGER"
            indexes = indexes.union(self.indexes[f"HAND_{name}{'_CONNECTIONS' if connections else ''}"].value)

        if not inplace:
            image = image.copy()
        height, width = self.landmarks.image.shape[:2]
        for index in indexes:
            if isinstance(index, tuple):
                pts = self.landmarks.get_points(index)

                pt1 = pts[0]
                pt1 = normalize_pixel(pt1[0], pt1[1], width, height)

                pt2 = pts[1]
                pt2 = normalize_pixel(pt2[0], pt2[1], width, height)

                image = cv2.line(image, pt1, pt2, color, thickness)
            else:
                pts = self.landmarks.get_points([index])

            for point in pts:
                pt = normalize_pixel(point[0], point[1], width, height)
                norm = min(max((point[2] + 1), 0), 1)
                radius = int(point_scale[0] + ((1 - norm) * (point_scale[1] - point_scale[0])))
                image = cv2.circle(image, pt, radius, color, -1)
        
        return image