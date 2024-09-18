import numpy as np

from collections import namedtuple
from typing import List, NamedTuple, Optional

from .hand import Hand

from ..constants import CONFIG, MP_HAND_MESH
from ..enums import SideEnum
from ..landmarks import Landmarks

class Tracking:
    def __init__(self,
                 static_image_mode=False,
                 max_num_hands=2,
                 model_complexity=1,
                 min_detection_confidence=0.5,
                 min_tracking_confidence=0.5) -> None:
        self.handsmesh = MP_HAND_MESH.Hands(
            static_image_mode,
            max_num_hands,
            model_complexity,
            min_detection_confidence,
            min_tracking_confidence)
        
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
            
        hands = self.handsmesh.process(image)
        if hands.multi_hand_landmarks:
            Result = namedtuple('hand', ['classification', 'landmarks', 'image'])
            return [Result(classification=hand.classification[0],
                           landmarks=marks.landmark,
                           image=image)
                    for hand, marks
                    in zip(hands.multi_handedness, hands.multi_hand_landmarks)]
        return[]