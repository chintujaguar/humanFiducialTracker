#!/usr/bin/env python
import rospy
from std_msgs import String
from geometry_msgs import Twist
from fiducial_msgs import Fiducials
from fiducial_msgs import FiducialTransforms
from sensor_msgs import CompressedImage
from sensor_msgs import CameraInfo

# Control class for controlling the movement of turtlebot
class Control():
    # Constructor fro Control class
    def __init__(self):
        Twist self.velocity
        self.direct = 0
        cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        
    # Set forward velocity of the robot, pass negative value to move backward
    def set_vel(self, vel):
        velocity.linear.x = vel
        vel_str = "Moving with velocity %s" % vel
        rospy.loginfo(vel_str)
        cmd_vel.publish(velocity)
        rate.sleep()

    # Set positive to take right turn, or negative to take a left turn
    def set_dir(self, dir, angle):
        if dir == "left":
            self.direct = -1
        else:
            self.direct = 1
        velocity.angular.z = direct*angle
        vel_str = "Moving in direction" + dir
        rospy.loginfo(vel_str)
        vel_str = "with angular velocity %s" % angle
        rospy.loginfo(vel_str)
        cmd_vel.publish(velocity)

    # Set velocity zero to stop robot
    def set_vel_zero():
        velocity.linear.x = 0
        vel_str = "Stopping the robot"
        rospy.loginfo(vel_str)
        cmd_vel.publish(velocity)

def main():
    rospy.init_node('turtle_controller', anonymous=True)
    tc = Control()
    tc.set_dir("left", 1)
    tc.set_vel(1)

    rate = rospy.Rate(10) # 10 Hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        while not rospy.is_shutdown():


if __name__ == "__main__"
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