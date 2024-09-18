import pytest

from tracking.config import Config
from tracking.exceptions import IncorrectInstanceException

@pytest.mark.parametrize("value", [
    100.23,
    [1920],
    (1080,),
    "1920x1080",
    '0',
])
def test_screen_width_setter_if_raise_incorrect_instance_exception(value):
    config = Config()
    with pytest.raises(IncorrectInstanceException):
        config.SCREEN_WIDTH = value
    
@pytest.mark.parametrize("value", [
    100.23,
    [1920],
    (1080,),
    "1920x1080",
    '0',
])
def test_screen_height_setter_if_raise_incorrect_instance_exception(value):
    config = Config()
    with pytest.raises(IncorrectInstanceException):
        config.SCREEN_HEIGHT = value

@pytest.mark.parametrize("value", [
    100.23,
    [1920],
    (1080,),
    "1920x1080",
    '0',
])
def test_video_capture_setter_if_raise_incorrect_instance_exception(value):
    config = Config()
    with pytest.raises(IncorrectInstanceException):
        config.VIDEO_CAPTURE = value