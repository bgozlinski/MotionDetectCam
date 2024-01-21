import os
from abc import ABC, abstractmethod
import cv2 as cv


class FileHandler(ABC):
    """
    Abstract base class for handling file operations related to images.
    """
    @abstractmethod
    def save(self, image, path) -> None:
        """
        Abstract method to save an image with flexibility in file path and format.

        :param image: Image to be saved.
        :param path: File path including the filename where the image will be saved.
        """
        pass


class SaveImage(FileHandler):
    """
    Concrete implementation of FileHandler to save an image with support for multiple formats.
    """
    def save(self, image, path) -> None:
        """
        Saves an image with the provided path and format. Format is inferred from the file extension.

        :param image: Image to be saved.
        :param path: File path including the filename where the image will be saved.
        """
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        cv.imwrite(path, image)
