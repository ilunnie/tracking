import mediapipe as mp
import numpy as np
import os
import pkg_resources

from typing import List, Optional

from . import BaseOptions, FaceLandmarker, FaceLandmarkerOptions, FaceLandmarkerResult
from .face import Face

from .. import CONFIG
from ..abstract_tracking import AbstractTracking
from ..enums import RunningModeEnum
from ..landmarks import Landmarks

class Tracking(AbstractTracking):
    def __init__(self,
                 running_mode: RunningModeEnum = RunningModeEnum.IMAGE,
                 max_num_faces: int = 1,
                 min_face_detection_confidence: float = 0.5,
                 min_face_presence_confidence: float = 0.5,
                 min_tracking_confidence: float = 0.5,
                 output_face_blendshapes: bool = False,
                 output_facial_transformation_matrixes: bool = False,
                 result_callback = None,
                 task_path:Optional[str] = None) -> None:
        
        if task_path is None:
            task_path = pkg_resources.resource_filename(__name__, '')
            task_path = os.path.join(os.path.dirname(task_path), "tasks", "face_landmarker.task")
        base_options = BaseOptions(model_asset_path=task_path)
        options = FaceLandmarkerOptions(base_options=base_options,
                                        running_mode=running_mode,
                                        num_faces=max_num_faces,
                                        min_face_detection_confidence=min_face_detection_confidence,
                                        min_face_presence_confidence=min_face_presence_confidence,
                                        min_tracking_confidence=min_tracking_confidence,
                                        output_face_blendshapes=output_face_blendshapes,
                                        output_facial_transformation_matrixes=output_facial_transformation_matrixes,
                                        result_callback=(self.callback if running_mode == RunningModeEnum.LIVE_STREAM else None))
        super().__init__(FaceLandmarker.create_from_options(options), result_callback)
        
    def callback(self,
                 result: FaceLandmarkerResult,
                 image: mp.Image,
                 timestamp: int):
        self.__faces = [Face(Landmarks(image.numpy_view(), face)) for face in result.face_landmarks]
        return super().callback(result, self.__faces, image, timestamp)
    
    def predict(self, image: Optional[np.ndarray] = None) -> List[Face]:
        if image is None:
            _, image = CONFIG.VIDEO_CAPTURE.read()
            
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        
        self.detect(image)
        return self.__faces
    
    def detect(self, image: mp.Image) -> FaceLandmarkerResult:
        return super().detect(image)
