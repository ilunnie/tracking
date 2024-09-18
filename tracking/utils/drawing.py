from numbers import Number
from typing import Union

from ..constants import CONFIG, MP_DRAWING

def normalize_pixel(
        x: Union[Number],
        y: Union[Number],
        width: Union[Number] = None,
        height: Union[Number] = None):
    
    return MP_DRAWING._normalized_to_pixel_coordinates(
        x, y,
        width or CONFIG.VIDEO_CAPTURE.width,
        height or CONFIG.VIDEO_CAPTURE.height)