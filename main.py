import time
import os
import fpstimer
from playsound import playsound
from pynput.keyboard import Key, Controller
from image_converting import get_list
from create_directory_with_frames import get_frames_from_video


if __name__ == "__main__":
    keyboard = Controller()
    confirm_full_screen = input("Full screen? Y/n: ")
    if confirm_full_screen == 'Y':
        keyboard.press(Key.f11)
        keyboard.release(Key.f11)

    confirm_frames = input("Need frames? Y/n: ")
    if confirm_frames == 'Y':
        get_frames_from_video()

    confirm_sound = input("Play with sound? Y/n: ")

    # getting list with names of frames
    directory = f"{os.path.dirname(os.path.abspath(__file__))}\\frames"
    list_with_frame_names = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            list_with_frame_names.append([filename, int(filename[0:-4])])

    # list sorting in increasing order
    list_with_frame_names = sorted(list_with_frame_names, key=lambda x: x[1])

    # calculating output
    out_list = []
    columns, rows = os.get_terminal_size()
    print("Calculating output")
    for i in list_with_frame_names:
        out_list.append(get_list("frames/" + i[0], columns, rows))
    print("done")
    time.sleep(1)

    if confirm_sound == 'Y':
        audio_file = f"{os.path.dirname(os.path.abspath(__file__))}\\bad_apple_audio.mp3"
        playsound(audio_file, False)

    FPS = 30
    timer = fpstimer.FPSTimer(FPS)
    num_of_frames = len(list_with_frame_names)
    for i in range(num_of_frames):
        print(out_list.pop(0), end='')
        timer.sleep()

    time.sleep(5)
