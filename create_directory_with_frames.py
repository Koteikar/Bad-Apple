import cv2
import os


def get_frames_from_video():
    directory_name = "frames"
    os.mkdir(directory_name)
    vid_cap = cv2.VideoCapture("video.mp4")
    success, image = vid_cap.read()
    count = 0
    while success:
        # save frame as JPEG file
        cv2.imwrite(f"{directory_name}/{count}.jpg", image)
        success, image = vid_cap.read()
        print("Read a new frame: ", count)
        count += 1
