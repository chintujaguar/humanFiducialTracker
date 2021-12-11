#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from fiducial_msgs.msg import FiducialArray
from fiducial_msgs.msg import FiducialTransformArray
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import CameraInfo

# Control class for controlling the movement of turtlebot
class Control():
    # Constructor for Control class
    def __init__(self):
        self.velocity = Twist()
        self.direct = 0
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.x_vert = 0
        self.depth = 0
        self.side = 0
        rospy.Subscriber('/fiducial_vertices', FiducialArray, self.fid_vert_cb)
        rospy.Subscriber('/fiducial_transforms', FiducialTransformArray, self.fid_trans_cb)

    def infinite_loop(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            print("depth in main: ", self.depth)
            self.set_dir(self.x_vert)
            self.set_vel(self.depth)
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            # pub.publish(hello_str)
            rate.sleep()

    # Set forward velocity of the robot based on x value
    def set_vel(self, x):
        print("depth in set_vel: ", x)
        if x > 5:
            self.velocity.linear.x = 2
        elif x < 0.75:
            self.set_vel_zero()
        else:  
            self.velocity.linear.x = 0.1 # If possible, make this smoother by changing velocity according to x value
        self.vel_str = "Moving with velocity %s" % self.velocity.linear.x
        rospy.loginfo(self.vel_str)
        self.cmd_vel.publish(self.velocity)

    # Set angular velocity based on y coordinate of aruco top left vertex in image frame
    def set_dir(self, y):
        # wheel_base = 0.3
        if y < 620: # Object to the left
            self.velocity.angular.z = 0.25
        elif y > 630: # Object to the right
            self.velocity.angular.z = -0.25
        else:
            self.set_vel_zero()
        vel_str = "Moving in direction" # + dir
        rospy.loginfo(vel_str)
        vel_str = "with angular velocity %s" #% angle
        rospy.loginfo(vel_str)
        self.cmd_vel.publish(self.velocity)

    # Set velocity zero to stop robot
    def set_vel_zero(self):
        self.velocity.linear.x = 0
        self.velocity.angular.z = 0
        vel_str = "Stopping the robot"
        rospy.loginfo(vel_str)
        self.cmd_vel.publish(self.velocity)

    def fid_vert_cb(self, msg):
        # rospy.loginfo("SUBSCRIBING TO FID VERT TOPIC")
        fid_array = FiducialArray()
        fid_array = msg
        if len(fid_array.fiducials) >= 1:
            self.x_vert = fid_array.fiducials[0].x0
        else:
            self.x_vert = 625
        # rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg)

    def fid_trans_cb(self, msg):
        # rospy.loginfo("SUBSCRIBING TO FID TRANS TOPIC")
        transform = FiducialTransformArray()
        transform = msg
        if len(transform.transforms) >= 1:
            self.depth = transform.transforms[0].transform.translation.z
            self.side = transform.transforms[0].transform.translation.x
        else:
            self.depth = 0.1
            self.side = 0
        # rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg)

# def aruco_get():
#     rospy.Subscriber('/fiducial_vertices', FiducialArray, fid_vert_cb)
#     rospy.Subscriber('/fiducial_transforms', FiducialTransformArray, fid_trans_cb)

def main():
    rospy.init_node('turtle_controller', anonymous=True)
    # aruco_get()
    rate = rospy.Rate(10) # 10 Hz
    tc = Control()
    # cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    # velocity = Twist()
    # velocity.linear.x = 0.1
    # velocity.angular.z = 0.1
    # cmd_vel.publish(velocity)
    print('Before while')
    tc.infinite_loop()
    # while not rospy.is_shutdown():
    #     print("depth in main: ", depth)
    #     # tc.set_dir(x_vert)
    #     tc.set_vel(depth)
    #     hello_str = "hello world %s" % rospy.get_time()
    #     rospy.loginfo(hello_str)
    #     # pub.publish(hello_str)
    #     rate.sleep()
    
    rospy.spin()

if __name__ == '__main__':
    # global depth
    # global side
    # x_vert = 0
    # depth = 0
    main()



# license removed for brevity
# import rospy
# from std_msgs.msg import String

# def talker():
#     pub = rospy.Publisher('chatter', String, queue_size=10)
#     rospy.init_node('talker', anonymous=True)
#     rate = rospy.Rate(10) # 10hz

#         

# if __name__ == '__main__':
#     try:
#         talker()
#     except rospy.ROSInterruptException:
#         pass

###### NOTES ######
# The camera tf frame:
# x points outwards
# y points to the left
# z points upwards

# 624 (x) x 188 (y) is the center point of the image