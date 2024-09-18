from enum import Enum

from ..hand_tracking.constants import HandIndexes

class FingerEnum(Enum):
    THUMB   = 0
    INDEX   = 1
    MIDDLE  = 2
    RING    = 3
    PINKY   = 4

    @classmethod
    def get_tip(cls, finger: 'FingerEnum') -> int:
        name = finger.name if finger == cls.THUMB else finger.name + "_FINGER"
        return HandIndexes[f"HAND_{name}_TIP"].value

    @classmethod
    def get_points(cls, finger: 'FingerEnum') -> tuple:
        name = finger.name if finger == cls.THUMB else finger.name + "_FINGER"
        return HandIndexes[f"HAND_{name}"].value
    
    @classmethod
    def get_connections(cls, finger: 'FingerEnum') -> set:
        name = finger.name if finger == cls.THUMB else finger.name + "_FINGER"
        return  HandIndexes[f"HAND_{name}_CONNECTIONS"].value