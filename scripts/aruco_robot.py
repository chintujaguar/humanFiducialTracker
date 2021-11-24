#!/usr/bin/env python3
# This node is to implement a basic aruco detection using the turtlebot camera

# Subscribe to the /camera/rgb/compressed topic
# Publish this onto /camera/compressed topic

# Subscribe to the /camera/rgb/camera_info topic
# Publish this onto /camera_info topic

# Subscribe to /fiducial_vertices topic
# Subscribe to /fiducial_transforms topic

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from fiducial_msgs.msg import Fiducials
from fiducial_msgs.msg import FiducialTransforms
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import CameraInfo


def turt_vid_cb(msg):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)
    img.publish(msg)

def turt_cam_info_cb(msg):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)
    cam_info.publish(msg)    

    
def aruco_get():
    rospy.init_node('aruco_robot', anonymous=True)
    rospy.Subscriber("/camera/rgb/compressed", CompressedImage, turt_vid_cb)
    global img = rospy.Publisher('/camera/compressed', CompressedImage, queue_size=10)
    rospy.Subscriber("/camera/rgb/camera_info", CameraInfo, turt_cam_info_cb)
    global cam_info = rospy.Publisher('/camera_info', CameraInfo, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    aruco_get()


