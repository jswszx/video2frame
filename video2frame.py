import os
import sys
import shutil
import cv2

def video2frame(video_dir, v_file, set_fps):
    # Set the directory where captured images are outputed
    img_dir = './image_dir/'
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    # Instance
    cap = cv2.VideoCapture(os.path.join(video_dir, v_file))
    # Get the fps and the number of frames
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # Calculate the number of frames to skip
    step_frame = int(fps/set_fps)

    # Capture into frames
    i = 0
    for n in range(0, frame_n, step_frame):
        cap.set(cv2.CAP_PROP_POS_FRAMES, n)
        ret, frame = cap.read()  # Capture frame-by-frame
        if ret == False:  # Is a frame left?
            break
        # Save
        file_name = os.path.splitext(v_file)[0]
        image_path = "{:}_{:0>3}.png".format(os.path.join(img_dir, file_name), i)
        cv2.imwrite(image_path, frame)
        print('Saved:', image_path)
        i += 1

    cap.release()

if __name__ == "__main__":
    # ROOT
    # ├── video2frame.py
    # ├── dataset
    # │    ├── a.MOV
    # │    ├── b.mp4
    # │    └── c.avi
    # └── image_dir
    #      ├── a_000.png
    #      └── a_001.png
    #
    # Directory path where videos are stored
    video_dir = './dataset/'
    # Set the fps
    if len(sys.argv) == 2:
        set_fps = float(sys.argv[1])
    else:
        set_fps = 10    # default
    # Run
    exts = ['.mp4', '.avi', '.MOV']
    for v_file in os.listdir(video_dir):
        if v_file.endswith(tuple(exts)):
            video2frame(video_dir, v_file, set_fps)
