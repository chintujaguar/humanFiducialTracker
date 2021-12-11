#!/usr/bin/env python3
# This node is to implement a basic aruco detection using the turtlebot camera

# Subscribe to the /camera/rgb/image_raw/compressed topic
# Publish this onto /camera/compressed topic

# Subscribe to the /camera/rgb/camera_info topic
# Publish this onto /camera_info topic

# Subscribe to /fiducial_vertices topic
# Subscribe to /fiducial_transforms topic

import rospy
import numpy as np
from tf.transformations import quaternion_matrix
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Transform
from fiducial_msgs.msg import FiducialArray
from fiducial_msgs.msg import FiducialTransformArray
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import CameraInfo

global x_initial,z_initial

def turt_vid_cb(msg):
    rospy.loginfo("SUBSCRIBING TO COMPRESSED IMAGE TOPIC")
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg)
    # img.publish(msg)

def turt_cam_info_cb(msg):
    rospy.loginfo("SUBSCRIBING TO CAM INFO TOPIC")
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg)
    # cam_info.publish(msg)

def fid_vert_cb(msg):
    rospy.loginfo("SUBSCRIBING TO FID VERT TOPIC")
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg)

def fid_trans_cb(msg):
    # rospy.loginfo("SUBSCRIBING TO FID TRANS TOPIC")
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg)
    # print(msg.transforms[0].transform.translation.x)
    # rotation_matrix = quaternion_matrix([msg.transforms[0].transform.rotation.x,msg.transforms[0].transform.rotation.y,msg.transforms[0].transform.rotation.z,msg.transforms[0].transform.rotation.w])
    # print('Rotation Matrix= {}'.format(rotation_matrix))
    # rotation_matrix = rotation_matrix[0:3,0:3]
    # rotation_matrix_inv = np.linalg.pinv(rotation_matrix)
    # print(rotation_matrix)
    # xyz = np.c_[[msg.transforms[0].transform.translation.x,msg.transforms[0].transform.translation.y,msg.transforms[0].transform.translation.z]]
    # # print('xyz={}'.format(xyz.shape))
    # Translations = -1 * np.matmul(rotation_matrix_inv,xyz)
    # print(Translations)
    # H = np.concatenate([rotation_matrix_inv,Translations],axis = 1)
    # row = np.array([[0,0,0,1]])
    # coordinates = np.c_[[0,0,0,1]]
    # # print(xyz.shape)
    # # print(row.shape)
    # H = np.concatenate([H,xyz], axis = 0)
    # print(H)
    # xyz_camera = np.matmul(rotation_matrix_inv,xyz)
    # print(xyz_camera)
    z = msg.transforms[0].transform.translation.z
    x = msg.transforms[0].transform.translation.x
    x_initial = 0
    z_initial = 0
    



    
def aruco_get():
    rospy.init_node('aruco_robot', anonymous=True)
    global cam_info
    global img
    # cam_info = rospy.Publisher('/camera_info', CameraInfo, queue_size=10)
    # img = rospy.Publisher('/camera/compressed', CompressedImage, queue_size=10)
    # rospy.Subscriber('/camera/rgb/image_raw/compressed', CompressedImage, turt_vid_cb)
    # rospy.Subscriber('/camera/rgb/camera_info', CameraInfo, turt_cam_info_cb)
    # rospy.Subscriber('/fiducial_vertices', FiducialArray, fid_vert_cb)
    rospy.Subscriber('/fiducial_transforms', FiducialTransformArray, fid_trans_cb)
    rospy.spin()

if __name__ == '__main__':
    aruco_get()


