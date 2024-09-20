from numbers import Number
from typing import Union

from mediapipe.python.solutions import drawing_utils

from .. import CONFIG

def normalize_pixel(
        x: Union[Number],
        y: Union[Number],
        width: Union[Number] = None,
        height: Union[Number] = None):
    
    return drawing_utils._normalized_to_pixel_coordinates(
        x, y,
        width or CONFIG.VIDEO_CAPTURE.width,
        height or CONFIG.VIDEO_CAPTURE.height)