#!/usr/bin/env python3
#This node is to make the turtlebot move using a simple script
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def turt_move():
    cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('basic_move', anonymous=True)
    velocity = Twist()

    while not rospy.is_shutdown():
        velocity.linear.x = 1
        velocity.angular.z = 1
        cmd_vel.publish(velocity)
        hello_str = "Moving forward"
        rospy.loginfo(hello_str)
        rospy.sleep(3)

        velocity.linear.x = -1
        velocity.angular.z = -1
        cmd_vel.publish(velocity)
        hello_str = "Moving backward"
        rospy.loginfo(hello_str)
        rospy.sleep(3)

if __name__ == '__main__':
    try:
        turt_move()
    except rospy.ROSInterruptException:
        pass