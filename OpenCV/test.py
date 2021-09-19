#!/usr/bin/env python3

import cv2 as cv

image_path = '/home/maxime/Python/OpenCV/Images/Lenna.png'
winname = "OpenCV_Restitution_{image_path}"


class COMPUTER_VISION():
    """
    TODO:
    """
    def init_webcam(index):
        """
        Initialize webcam device capture
        
        :param  index: video capture device index
        """
        capture_webcam = cv.VideoCapture(index)
        return capture_webcam

    def take_webcam_picture(capture_video, mirror=False):
        """
        TODO:
        """
        _, video = capture_video.read()
        if mirror:
            video = cv.flip(video, 1)
        return video

    def init_image(image="/home/maxime/Python/OpenCV/Images/not_found.png", color_mode="IMREAD_COLOR"):
        """
        TODO:
        """
        image = cv.imread(image_path, color_mode)
        return image


    def print_image(image_path, windows_name=image_path):
        """
        TODO:
        """
        while(True):
            cv.imshow(windows_name, image_path)
            if cv.waitKey(1) == 27:
                break
        cv.destroyAllWindows()


def main():
    webcam_init = COMPUTER_VISION.init_webcam(0)
    video = COMPUTER_VISION.take_webcam_picture(webcam_init, mirror=False)
    COMPUTER_VISION.print_image(video, windows_name="Webcam")

    
if __name__ == "__main__":
    main()