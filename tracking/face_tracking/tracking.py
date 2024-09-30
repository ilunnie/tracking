import mediapipe as mp
import numpy as np
import os
import pkg_resources

from threading import Event
from typing import List, Optional

from . import BaseOptions, FaceLandmarker, FaceLandmarkerOptions, FaceLandmarkerResult
from .face import Face

from ..enums import RunningModeEnum

class Tracking:
    def __init__(self,
                 running_mode: RunningModeEnum = RunningModeEnum.IMAGE,
                 max_num_faces: int = 1,
                 min_face_detection_confidence: float = 0.5,
                 min_face_presence_confidence: float = 0.5,
                 min_tracking_confidence: float = 0.5,
                 output_face_blendshapes: bool = False,
                 output_facial_transformation_matrixes: bool = False,
                 result_callback = None,
                 task_path:str = None) -> None:
        
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
        self.facesmesh = FaceLandmarker.create_from_options(options)
        self.__running_mode = running_mode
        self.__timestamp = 0
        self.__lastupdate = None
        self.__result_callback = result_callback
        self.__callback = Event()
        
    def callback(self,
                    result: FaceLandmarkerResult,
                    image: mp.Image,
                    timestamp: int):
        #TODO implement later
        raise NotImplementedError("callback method not implemented")
    
    def predict(self, image: Optional[np.ndarray] = None) -> List[Face]:
        #TODO implement later
        raise NotImplementedError("predict method not implemented")
    
    def detect(self, image: mp.Image) -> FaceLandmarkerResult:
        #TODO implement later
        raise NotImplementedError("detect method not implemented")
