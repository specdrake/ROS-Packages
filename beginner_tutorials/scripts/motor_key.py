#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
from getkey import getkey, keys
def talker():
    pub = rospy.Publisher('servo', UInt16, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        pub.publish(0)
        x = 0
        while True:
            print "Press up or down: "
            key = getkey()
            if key == keys.UP and x >= 0 and x <= 170:
                x+=10
                rospy.loginfo(x)
                pub.publish(x)
            if key == keys.DOWN and x >= 10 and x<=180:
                x-=10
                rospy.loginfo(x)
                pub.publish(x)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

