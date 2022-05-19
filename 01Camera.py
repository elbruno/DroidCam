# Bruno Capuano 2022
# display the camera feed using OpenCV
# add some sample changes

import time
import cv2
import argparse

# read command line arguments
parser = argparse.ArgumentParser()

# add string argument for ip address
parser.add_argument("--ip", help="camera ip address", default="")
args = parser.parse_args()

# get first argument
ip = args.ip

# print ip address
print("ip address:", ip)
print("press q to quit")


# Camera Settings
camera_Width  = 640 # 1024 # 1280 # 640
camera_Heigth = 480 # 780  # 960  # 480
frameSize = (camera_Width, camera_Heigth)
#video_capture = cv2.VideoCapture(f"http://192.168.1.240:4747/video")
video_capture = cv2.VideoCapture(f"http://{ip}:4747/video")
time.sleep(1.0)

while True:
    ret, frameOrig = video_capture.read()
    frame = cv2.resize(frameOrig, frameSize)
  
    cv2.imshow(f"@elbruno - Camera [{ip}]", frame)

    # key controller
    key = cv2.waitKey(1) & 0xFF    
    if key == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()