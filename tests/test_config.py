import os
import cv2
import numpy as np
import pytest

from tracking.config import Config
from tracking.webcam import WebCam

@pytest.mark.parametrize("value", [
    1920, 1000, 720, 1080
])
def test_screen_width_accepts_valid_value(value):
    config = Config()
    config.SCREEN_WIDTH = value
    assert config.SCREEN_WIDTH == value

@pytest.mark.parametrize("value", [
    1920, 1000, 720, 1080
])
def test_screen_height_accepts_valid_value(value):
    config = Config()
    config.SCREEN_HEIGHT = value
    assert config.SCREEN_HEIGHT == value

def test_video_capture_accepts_valid_value():
    config = Config()
    video_path = os.path.join(os.path.dirname(__file__), 'test_data', 'SampleVideo_1280x720_1mb.mp4')
    
    cap = cv2.VideoCapture(video_path)
    config.VIDEO_CAPTURE = WebCam(cap)

    assert config.VIDEO_CAPTURE.isOpened == True
    
    sucess, frame = config.VIDEO_CAPTURE.read()
    assert (sucess, type(frame)) == (True, np.ndarray)

    assert config.VIDEO_CAPTURE.shape == (1280, 720)
    assert config.VIDEO_CAPTURE.width == 1280
    assert config.VIDEO_CAPTURE.height == 720

    config.VIDEO_CAPTURE.close()
    assert config.VIDEO_CAPTURE.isOpened == False