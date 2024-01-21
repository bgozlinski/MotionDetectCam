from camera import WebCamera, DisplayCamera
from motion_detector import MOG2MotionDetector
from filehandler import SaveImage
import cv2 as cv


def main(camera, display, motion_detector) -> None:
    """
    Main application function to capture and display camera frames.

    :param camera: The camera object to capture frames.
    :param display: The display object to show frames.
    :param motion_detector: The motion detector algorithm to use to detect motion.
    """
    warmup_frames = 100  # Number of frames to wait before starting motion detection
    frame_count = 0

    try:
        while True:
            frame = camera.get_frame()
            motion_detected, fg_mask = motion_detector.detect(frame)

            if frame_count > warmup_frames:
                if motion_detected:
                    print("Motion detected!")
                    SaveImage().save(frame, 'output/test.jpg')
            else:
                frame_count += 1

            display.show_comparison(window_name='name', frames=[frame, fg_mask])
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        camera.release()
        cv.destroyAllWindows()


if __name__ == '__main__':
    camera = WebCamera()
    display = DisplayCamera()
    motion_detector = MOG2MotionDetector()
    main(camera, display, motion_detector)
