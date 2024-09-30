import cv2
import numpy as np
import mediapipe as mp

from collections import namedtuple
from datetime import datetime
from threading import Event
from typing import Callable, List, NamedTuple, Optional

from . import BaseOptions, HandLandmarker, HandLandmarkerOptions, HandLandmarkerResult
from .hand import Hand

from .. import CONFIG
from ..enums import SideEnum, RunningModeEnum
from ..landmarks import Landmarks

class Tracking:
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
                         int], None]] = None) -> None:
        
        base_options = BaseOptions(model_asset_path='./tasks/hand_landmarker.task')
        options = HandLandmarkerOptions(base_options=base_options,
                                        running_mode=running_mode,
                                        num_hands=max_num_hands,
                                        min_hand_detection_confidence=min_hand_detection_confidence,
                                        min_hand_presence_confidence=min_hand_presence_confidence,
                                        min_tracking_confidence=min_tracking_confidence,
                                        result_callback=(self.callback if running_mode == RunningModeEnum.LIVE_STREAM else None))
        self.handsmesh = HandLandmarker.create_from_options(options)
        self.__running_mode = running_mode
        self.__timestamp = 0
        self.__lastupdate = None
        self.__result_callback = result_callback
        self.__callback = Event()
        
    def callback(self, 
                 result: HandLandmarkerResult, 
                 image: mp.Image, 
                 timestamp: int):
        self.__result = result

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
        
        self.__callback.set()
        if self.__result_callback:
            self.__result_callback(self.__hands, image, timestamp)

    def predict(self, image: Optional[np.ndarray] = None, side_mirror = False) -> List[Hand]:
        self.__side_mirror = side_mirror
        if image is None:
            _, image = CONFIG.VIDEO_CAPTURE.read()
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)

        self.detect(image)
        return self.__hands
    
    def detect(self, image: mp.Image) -> HandLandmarkerResult:
        self.__callback.clear()
        if self.__running_mode == RunningModeEnum.LIVE_STREAM:
            now = datetime.now()
            if self.__lastupdate:
                self.__timestamp += int((now - self.__lastupdate).total_seconds() * 1000)
                self.__lastupdate = now
            else:
                self.__timestamp = 0
                self.__lastupdate = now
            self.handsmesh.detect_async(image, self.__timestamp)
        else:
            if self.__running_mode == RunningModeEnum.IMAGE:
                result = self.handsmesh.detect(image)
            else:
                self.__timestamp += 1
                result = self.handsmesh.detect_for_video(image, self.__timestamp)
            self.callback(result, image, self.__timestamp)

        self.__callback.wait()
        return self.__result