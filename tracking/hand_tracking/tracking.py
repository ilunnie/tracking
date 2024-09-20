from datetime import datetime
import numpy as np
import mediapipe as mp

from collections import namedtuple
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
                         HandLandmarkerResult,
                         np.ndarray,
                         int], None]] = None) -> None:
        
        base_options = BaseOptions(model_asset_path='./tasks/hand_landmarker.task')
        options = HandLandmarkerOptions(base_options=base_options,
                                                     running_mode=running_mode,
                                                     num_hands=max_num_hands,
                                                     min_hand_detection_confidence=min_hand_detection_confidence,
                                                     min_hand_presence_confidence=min_hand_presence_confidence,
                                                     min_tracking_confidence=min_tracking_confidence,
                                                     result_callback=((lambda result, _, timestamp: result_callback(result, self.__image, timestamp))
                                                                      if result_callback else None))
        self.handsmesh = HandLandmarker.create_from_options(options)
        self.__running_mode = running_mode
        self.__timestamp = 0
        self.__lastupdate = None

    def predict(self, image: Optional[np.ndarray] = None, side_mirror = False) -> List[Hand]:
        results = self.process(image)
        
        hands = [Hand((SideEnum.mirror(SideEnum.from_string(hand.label))
                       if side_mirror
                       else SideEnum.from_string(hand.label)),
                      Landmarks(image, marks))
                 for hand, marks, image
                 in results]
        
        return hands
        
    def process(self, image: Optional[np.ndarray] = None) -> List[NamedTuple]:
        if image is None:
            _, image = CONFIG.VIDEO_CAPTURE.read()
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        self.__image = image

        if self.__running_mode == RunningModeEnum.IMAGE:
            result = self.handsmesh.detect(mp_image)
        elif self.__running_mode == RunningModeEnum.VIDEO:
            self.__timestamp += 1
            result = self.handsmesh.detect_for_video(mp_image, self.__timestamp)
        else:
            if self.__lastupdate:
                now = datetime.now()
                self.__timestamp += now - self.__lastupdate
                self.__lastupdate = now
            else:
                self.__timestamp = 0
                self.__lastupdate = datetime.now()
            result = self.handsmesh.detect_async(mp_image, self.__timestamp)

        Result = namedtuple('hand', ['classification', 'landmarks', 'image'])
        return [Result(classification=hand[0].Category.display_name,
                       Landmarks=marks,
                       image=image)
                for hand, marks
                in zip(result.handedness, result.hand_landmarks)]