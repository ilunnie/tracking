import cv2
import numpy as np

from typing import Tuple

from ..abstract import FaceAbstract

from ...utils import normalize_pixel

class DrawingMethods(FaceAbstract):
    def draw(self, 
             image: np.ndarray, 
             color: Tuple[int, int, int],
             thickness: int = 1,
             connections: bool = True,
             points: bool = False,
             point_scale:Tuple[int, int] = (2, 25),
             inplace: bool = True):
        if not inplace:
            image = image.copy()
        height, width = self.landmarks.image.shape[:2]
    
        indexes = self.indexes[f'FACEMESH_TESSELATION{"_CONNECTIONS" if connections else ""}'].value
        for index in indexes:
            if isinstance(index, tuple):
                pts = self.landmarks.get_points(index)
                pt1, pt2 = pts
                
                pt1 = normalize_pixel(*pt1[:2], width, height)
                pt2 = normalize_pixel(*pt2[:2], width, height)
                
                if pt1 and pt2:
                    cv2.line(image, pt1, pt2, color, thickness)
            else:
                pts = self.landmarks.get_points([index])
                
            if points:
                for point in pts:
                    pt = normalize_pixel(point[0], point[1], width, height)
                    if pt is None:
                        continue
                    norm = min(max((point[2] + 1), 0), 1)
                    radius = int(point_scale[0] + ((1 - norm) * (point_scale[1] - point_scale[0])))
                    image = cv2.circle(image, pt, radius, color, -1)
                    
        return image
                
    
    def draw_contour(self,
                     image: np.ndarray,
                     color: Tuple[int, int, int],
                     thickness: int = 3,
                     internal: bool = False,
                     connections: bool = True,
                     points: bool = False,
                     point_scale:Tuple[int, int] = (5, 50),
                     inplace: bool = True):
        if not inplace:
            image = image.copy()
        height, width = self.landmarks.image.shape[:2]
        
        index_cat = f'FACEMESH_{"CONTOURS" if internal else "FACE_OVAL"}'
        indexes = self.indexes[(f'{index_cat}_CONNECTIONS' if connections else index_cat)].value
        for index in indexes:
            if isinstance(index, tuple):
                pts = self.landmarks.get_points(index)
                pt1, pt2 = pts
                
                pt1 = normalize_pixel(*pt1[:2], width, height)
                pt2 = normalize_pixel(*pt2[:2], width, height)
                
                if pt1 and pt2:
                    cv2.line(image, pt1, pt2, color, thickness)
            else:
                pts = self.landmarks.get_points([index])
                
            if points:
                for point in pts:
                    pt = normalize_pixel(point[0], point[1], width, height)
                    if pt is None:
                        continue
                    norm = min(max((point[2] + 1), 0), 1)
                    radius = int(point_scale[0] + ((1 - norm) * (point_scale[1] - point_scale[0])))
                    cv2.circle(image, pt, radius, color, -1)
                    
        return image