import cv2
import mediapipe as mp
import numpy as np
import os
import pkg_resources

from collections import namedtuple
from typing import Callable, List, Optional

from . import BaseOptions, HandLandmarker, HandLandmarkerOptions, HandLandmarkerResult
from .hand import Hand

from .. import CONFIG
from ..abstract_tracking import AbstractTracking
from ..enums import SideEnum, RunningModeEnum
from ..landmarks import Landmarks

class Tracking(AbstractTracking):
    def __init__(self,
                 running_mode: RunningModeEnum = RunningModeEnum.IMAGE,
                 max_num_hands: int = 1,
                 min_hand_detection_confidence: float = 0.5,
                 min_hand_presence_confidence: float = 0.5,
                 min_tracking_confidence: float = 0.5,
                 result_callback: Optional[
                     Callable[[
                         List[Hand],
                         mp.Image,
                         int], None]] = None,
                 task_path:Optional[str] = None) -> None:
        
        if task_path is None:
            task_path = pkg_resources.resource_filename(__name__, '')
            task_path = os.path.join(os.path.dirname(task_path), "tasks", "hand_landmarker.task")
        base_options = BaseOptions(model_asset_path=task_path)
        options = HandLandmarkerOptions(base_options=base_options,
                                        running_mode=running_mode,
                                        num_hands=max_num_hands,
                                        min_hand_detection_confidence=min_hand_detection_confidence,
                                        min_hand_presence_confidence=min_hand_presence_confidence,
                                        min_tracking_confidence=min_tracking_confidence,
                                        result_callback=(self.callback if running_mode == RunningModeEnum.LIVE_STREAM else None))
        super().__init__(HandLandmarker.create_from_options(options), result_callback)
        
    def callback(self, 
                 result: HandLandmarkerResult, 
                 image: mp.Image, 
                 timestamp: int):
        ResultTuple = namedtuple('hand', ['classification', 'landmarks', 'image'])
        results = [ResultTuple(classification=hand[0].display_name,
                                landmarks=marks,
                                image=image)
                        for hand, marks
                        in zip(result.handedness, result.hand_landmarks)]

        side_mirror = self.__side_mirror
        self.__hands = [Hand((SideEnum.mirror(SideEnum.from_string(hand))
                       if side_mirror
                       else SideEnum.from_string(hand)),
                      Landmarks(image.numpy_view(), marks))
                 for hand, marks, image
                 in results]
        
        super().callback(result, self.__hands, image, timestamp)

    def predict(self, image: Optional[np.ndarray] = None, side_mirror = False) -> List[Hand]:
        self.__side_mirror = side_mirror
        if image is None:
            _, image = CONFIG.VIDEO_CAPTURE.read()
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)

        self.detect(image)
        return self.__hands
    
    def detect(self, image: mp.Image) -> HandLandmarkerResult:
        return super().detect(image)