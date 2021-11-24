import cv2
import numpy as np
# import argparse
import sys
from utils import ARUCO_DICT, aruco_display

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="path to input image containing Aruco tag")
# ap.add_argument("-t", "--type", type=str, default="DICT_ARUCO_ORIGINAL", help="type of Aruco tag to detect")
# args = vars(ap.parse_args())

vid = cv2.VideoCapture(0)
arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT["DICT_4X4_100"])
arucoParams = cv2.aruco.DetectorParameters_create()

while(True):
    ret, frame = vid.read()
    corners, ids, rejected = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)
    detected_markers = aruco_display(corners, ids, rejected, frame)
    cv2.imshow('frame', detected_markers)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()



