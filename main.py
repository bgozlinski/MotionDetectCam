from camera import WebCamera, DisplayCamera
import cv2 as cv



def main(camera, display):
    """
    Main application function to capture and display camera frames.

    :param camera: The camera object to capture frames.
    :param display: The display object to show frames.
    """
    try:
        while True:
            frame = camera.get_frame()
            display.show_frame(frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        camera.release()
        cv.destroyAllWindows()


if __name__ == '__main__':
    camera = WebCamera()
    display = DisplayCamera()
    main(camera, display)
