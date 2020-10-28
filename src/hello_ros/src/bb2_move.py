#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

vel_msg = Twist()  

def setVel(vel_lx, vel_az):     
    vel_msg.linear.x = vel_lx
    vel_msg.angular.z = vel_az

def move():
    rospy.init_node('robot_bb8', anonymous=True)
    

    vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    
    setVel(0.3, 0.1)

    rate = rospy.Rate(10)
    rate.sleep()
    
    t1 = rospy.Time.now().to_sec()
    while not rospy.is_shutdown():        
        vel_publisher.publish(vel_msg)
        
        t2 = rospy.Time.now().to_sec()
        
    
        print(t2-t1)
        if t2-t1 > 10:
            setVel(0, 0)
            vel_publisher.publish(vel_msg)
            break
        rospy.sleep(1)
        
        



if __name__ == "__main__":
    try:
        move()
    except rospy.ROSInterruptException:
        print("Interrupt")
