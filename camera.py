import cv2 as cv
from abc import ABC, abstractmethod


class Camera(ABC):
    @abstractmethod
    def get_frame(self):
        pass

    @abstractmethod
    def release(self):
        pass


class WebCamera(Camera):
    def __init__(self, camera_index=0):
        self.cap = cv.VideoCapture(camera_index)

    def get_frame(self):
        if not self.cap.isOpened():
            raise Exception("Could not open camera")

        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Unable to read frame")

        return frame

    def release(self):
        self.cap.release()


class DisplayCamera:
    def show_frame(self, frame):
        cv.imshow('frame', frame)
