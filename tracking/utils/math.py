import numpy as np

from math import *

def center(points: list) -> tuple:
    points = np.mean(points, axis=0)
    return tuple(points)

def euclidean_distance(a: tuple, b: tuple) -> float:
    distance = np.sum([(a[i] - b[i]) ** 2 for i in range(len(a))])
    return sqrt(distance)

def direction(a, b) -> tuple:
    dir = [b - a for a, b in zip(a, b)]
    mag = sqrt(sum([d ** 2 for d in dir]))
    if mag == 0:
        return tuple(0 for _ in dir)
    return tuple(d / mag for d in dir)