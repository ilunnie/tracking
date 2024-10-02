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
    
    @staticmethod
    def direction(a, b) -> tuple:
        dir = [b - a for a, b in zip(a, b)]
        mag = math.sqrt(sum([d ** 2 for d in dir]))
        if mag == 0:
            return tuple(0 for _ in dir)
        return tuple(d / mag for d in dir)
    
for name, attr in [
        (name, getattr(math, name)) 
        for name in dir(math) 
        if not name.startswith('_')]:
    setattr(Math, name, attr)