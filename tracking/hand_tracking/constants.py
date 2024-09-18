import mediapipe as mp

from enum import Enum

class HandIndexes(Enum):
    HAND_PALM_CONNECTIONS = set(mp.solutions.hands_connections.HAND_PALM_CONNECTIONS)
    HAND_THUMB_CONNECTIONS = set(mp.solutions.hands_connections.HAND_THUMB_CONNECTIONS)
    HAND_INDEX_FINGER_CONNECTIONS = set(mp.solutions.hands_connections.HAND_INDEX_FINGER_CONNECTIONS)
    HAND_MIDDLE_FINGER_CONNECTIONS = set(mp.solutions.hands_connections.HAND_MIDDLE_FINGER_CONNECTIONS)
    HAND_RING_FINGER_CONNECTIONS = set(mp.solutions.hands_connections.HAND_RING_FINGER_CONNECTIONS)
    HAND_PINKY_FINGER_CONNECTIONS = set(mp.solutions.hands_connections.HAND_PINKY_FINGER_CONNECTIONS)

    HAND_PALM = tuple(sorted(set().union(*HAND_PALM_CONNECTIONS)))
    HAND_THUMB = tuple(sorted(set().union(*HAND_THUMB_CONNECTIONS)))
    HAND_INDEX_FINGER = tuple(sorted(set().union(*HAND_INDEX_FINGER_CONNECTIONS)))
    HAND_MIDDLE_FINGER = tuple(sorted(set().union(*HAND_MIDDLE_FINGER_CONNECTIONS)))
    HAND_RING_FINGER = tuple(sorted(set().union(*HAND_RING_FINGER_CONNECTIONS)))
    HAND_PINKY_FINGER = tuple(sorted(set().union(*HAND_PINKY_FINGER_CONNECTIONS)))

    HAND_THUMB_TIP = int(HAND_THUMB[-1])
    HAND_INDEX_FINGER_TIP = int(HAND_INDEX_FINGER[-1])
    HAND_MIDDLE_FINGER_TIP = int(HAND_MIDDLE_FINGER[-1])
    HAND_RING_FINGER_TIP = int(HAND_RING_FINGER[-1])
    HAND_PINKY_FINGER_TIP = int(HAND_PINKY_FINGER[-1])