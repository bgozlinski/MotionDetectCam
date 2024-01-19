import cv2 as cv
from abc import ABC, abstractmethod
import numpy as np
from config import config
from typing import List

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
    def show_frame(self, window_name: str, frame: np.ndarray) -> None:
        """
        Displays the given camera frame.

        :param window_name: The name of the window to show.
        :param frame: The camera frame to be displayed.
        """
        cv.imshow(window_name, frame)

    def show_comparison(self, window_name: str, frames: List) -> None:
        """
        Displays multiple frames combined horizontally in a single window.

        :param window_name: Name of the window in which to display the frames.
        :param frames: A list of frames (as NumPy arrays) to be combined and displayed.
        """
        combined_frame = np.hstack((frames[0], cv.cvtColor(frames[1], cv.COLOR_GRAY2BGR)))
        cv.imshow(window_name, combined_frame)
