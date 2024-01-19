import cv2 as cv
import numpy as np
from abc import ABC, abstractmethod
from config import config
from time import sleep


params = config(section='motion')


class MotionDetector(ABC):
    """
    Abstract base class for motion detection strategies.
    """
    @abstractmethod
    def detect(self, frame: np.ndarray) -> bool:
        """
        Detects motion in a camera frame.

        :param frame: The current camera frame as a NumPy array.
        :return: True if motion is detected, False otherwise.
        """
        pass


class MOG2MotionDetector(MotionDetector):
    """
    Motion detection using the MOG2 background subtraction method.
    """
    def __init__(self):
        self.background_subtractor = cv.createBackgroundSubtractorMOG2()

    def detect(self, frame: np.ndarray) -> [bool, np.ndarray]:

        """
        Applies MOG2 background subtraction to detect motion.

        :param frame: The current camera frame as a NumPy array.
        :return: True if motion is detected, False otherwise.
        """
        fg_mask = self.background_subtractor.apply(frame)
        _, thresh = cv.threshold(fg_mask, int(params['threshold']), 255, cv.THRESH_BINARY)
        contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv.contourArea(contour) > int(params['contours']):
                return True, thresh

        return False, thresh
        # return len(contours) > int(params['contours']), thresh
