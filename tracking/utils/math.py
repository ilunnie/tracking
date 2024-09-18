import math
import numpy as np

class Math:
    @staticmethod
    def center(points: list) -> tuple:
        points = np.mean(points, axis=0)
        return tuple(points)
    
    @staticmethod
    def euclidean_distance(a: tuple, b: tuple) -> float:
        distance = np.sum([(a[i] - b[i]) ** 2 for i in range(len(a))])
        return math.sqrt(distance)
    
for name, attr in [
        (name, getattr(math, name)) 
        for name in dir(math) 
        if not name.startswith('_')]:
    setattr(Math, name, attr)