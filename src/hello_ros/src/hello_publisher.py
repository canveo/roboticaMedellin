#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def move():
    rospy.init_node('robot_bb8', anonymous=True)

    vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    
    vel_msg = Twist()   
   
    while not rospy.is_shutdown():
        vel_msg.linear.x = 1
        vel_msg.linear.y = 1
        vel_publisher.publish(vel_msg)


if if __name__ == "__main__":
    try:
        move()
    except rospy.ROSInterruptException:
        pass
    


