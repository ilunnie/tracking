import cv2
import pytest
import tracking as tck

from tracking.hand_tracking import Tracking

@pytest.mark.parametrize(["image_path", "num_hands"], [
    (".\\tests\\test_data\\hand-pointing-at-object.jpg", 1),
    (".\\tests\\test_data\\hand-rejuventation.jpg", 2)
])
def test_hand_detection(image_path, num_hands):
    image = cv2.imread(image_path)

    tracking = Tracking(max_num_hands=10)
    hands = tracking.predict(image)

    assert len(hands) == num_hands

@pytest.mark.parametrize(["image_path", "results"], [(
        ".\\tests\\test_data\\hand-pointing-at-object.jpg", 
        [(True, True, False, False, False)]
    ), (
        ".\\tests\\test_data\\hand-rejuventation.jpg",
        [(True,) * 5] * 2
    )
    
])
def test_fingers_is_raised(image_path, results):
    image = cv2.imread(image_path)

    tracking = Tracking(max_num_hands=len(results))
    hands = tracking.predict(image)

    for result, hand in zip(results, hands):
        for r, finger in zip(result, tck.finger):
            assert r == hand.finger_is_raised(finger)