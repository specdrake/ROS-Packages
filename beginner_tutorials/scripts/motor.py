#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt16

def talker():
    pub = rospy.Publisher('servo', UInt16, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        x = 45
        while True:
            x = int(input("Enter a number: "))
            if x>180 or x < 0:
                continue
            else:
                break
        rospy.loginfo(x)
        pub.publish(x)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

