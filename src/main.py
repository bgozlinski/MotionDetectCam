from camera import WebCamera, DisplayCamera
from motion_detector import MOG2MotionDetector
import cv2 as cv


def main(camera, display):
    """
    Main application function to capture and display camera frames.

    :param camera: The camera object to capture frames.
    :param display: The display object to show frames.
    """
    motion_detector = MOG2MotionDetector()
    try:
        while True:
            frame = camera.get_frame()

            motion_detected, fg_mask = motion_detector.detect(frame)

            if motion_detected:
                print("Motion detected!")

            # display.show_frame('frame', frame)
            # display.show_frame('MOG2', fg_mask)
            display.show_comparison(window_name='name', frames=[frame, fg_mask])

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        camera.release()
        cv.destroyAllWindows()


if __name__ == '__main__':
    camera = WebCamera()
    display = DisplayCamera()
    main(camera, display)
