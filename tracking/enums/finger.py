from enum import Enum

class FingerEnum(Enum):
    THUMB   = 0
    INDEX   = 1
    MIDDLE  = 2
    RING    = 3
    PINKY   = 4

    @classmethod
    def get_tip(cls, finger: 'FingerEnum') -> int:
        from ..hand_tracking.constants import HandIndexes
        name = finger.name if finger == cls.THUMB else finger.name + "_FINGER"
        return HandIndexes[f"HAND_{name}_TIP"].value

    @classmethod
    def get_points(cls, finger: 'FingerEnum') -> tuple:
        from ..hand_tracking.constants import HandIndexes
        name = finger.name if finger == cls.THUMB else finger.name + "_FINGER"
        return HandIndexes[f"HAND_{name}"].value
    
    @classmethod
    def get_connections(cls, finger: 'FingerEnum') -> set:
        from ..hand_tracking.constants import HandIndexes
        name = finger.name if finger == cls.THUMB else finger.name + "_FINGER"
        return  HandIndexes[f"HAND_{name}_CONNECTIONS"].value