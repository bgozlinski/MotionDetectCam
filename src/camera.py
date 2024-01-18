import cv2 as cv
from abc import ABC, abstractmethod
import numpy as np
from config import config

params = config(section='camera')


class Camera(ABC):
    """
    Abstract base class representing a general camera interface.
    """

    @abstractmethod
    def get_frame(self) -> np.ndarray:
        """
        Captures and returns a single frame from the camera.
        """
        pass

    @abstractmethod
    def release(self) -> None:
        """
        Releases the camera resource.
        """
        pass


class WebCamera(Camera):
    """
    Concrete implementation of Camera for webcams.
    """

    def __init__(self, camera_index=int(params['port'])) -> None:
        """
        Initializes the camera object with the given camera index.

        :param camera_index: The index of the camera to use. Default is 0.
        """
        self.cap = cv.VideoCapture(camera_index)

    def get_frame(self) -> np.ndarray:
        """
        Captures and returns a frame from the webcam. Raises an exception if the camera cannot be accessed or frame cannot be read.

        :return: Captured camera frame.
        """
        if not self.cap.isOpened():
            raise Exception("Could not open camera")

        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Unable to read frame")

        return frame

    def release(self) -> None:
        """
        Releases the webcam resource.
        """
        self.cap.release()


class DisplayCamera:
    """
    A class for handling the display of camera frames.
    """
    def show_frame(self, frame: np.ndarray) -> None:
        """
        Displays the given camera frame.

        :param frame: The camera frame to be displayed.
        """
        cv.imshow('frame', frame)
