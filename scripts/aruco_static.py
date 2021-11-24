import cv2
import numpy as np
import argparse
import sys
from utils import ARUCO_DICT, aruco_display

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image containing Aruco tag")
ap.add_argument("-t", "--type", type=str, default="DICT_ARUCO_ORIGINAL", help="type of Aruco tag to detect")
args = vars(ap.parse_args())

image = cv2.imread(args["image"], 0)

# verify that the supplied Aruco tag exists and is supported by OpenCV
if ARUCO_DICT.get(args["type"], None) is None:
    print(f"Aruco tag type '{args['type']}' is not supported")
    sys.exit(0)

# load the Aruco dictionary, grab the Aruco parameters, and detect the markers
print("Detecting '{}' tags..." .format(args["type"]))
arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])
arucoParams = cv2.aruco.DetectorParameters_create()
corners, ids, rejected = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)

detected_markers = aruco_display(corners, ids, rejected, image)
cv2.imshow('image', detected_markers)

cv2.waitKey(0)
cv2.destroyAllWindows()

# arucoDict = aruco.Dictionary_get(aruco.DICT_6x6_50)
# arucoParams = aruco.DetectParameters_create()
# (corners, id, rejected) = aruco.detectMarkers(image, arucoDict, parameters=arucoParams)
