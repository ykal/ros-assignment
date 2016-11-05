#!/usr/bin/env python
import rospy
import time
import cv2
from SimpleCV import Camera
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String

def callback(img):
    bridge = CvBridge()
    try:
        image = bridge.imgmsg_to_cv2(img, "rgb8")
        image = cv2.cvtColor( image, cv2.COLOR_RGB2GRAY )
        rospy.loginfo("SAFE")
        cv2.imshow("Subscriber Frame", image)
        cv2.waitKey(1000)
    except CvBridgeError as e:
        rospy.loginfo(e)
    
    

def subscribe():
    subscriber = rospy.Subscriber("image_topic", Image, callback)
    rospy.spin()


def node():
    rospy.init_node("image_subscriber", anonymous=False)
    subscribe()


if __name__ == "__main__":
    node()
