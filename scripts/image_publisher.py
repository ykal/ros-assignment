#!/usr/bin/env python
import rospy
import time
import cv2
from SimpleCV import Camera
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String

rospy.init_node("image_publisher", anonymous=False)
rate = rospy.Rate(10000)
while not rospy.is_shutdown():
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.1) 
    return_value, image = camera.read()
    cv2.imwrite("opencv.png", image)
    del(camera)  
    bridge = CvBridge()
    publisher = rospy.Publisher('image_topic', Image, queue_size=1)
    try:
        image_msg = bridge.cv2_to_imgmsg(image, "rgb8")
        publisher.publish(image_msg)
        cv2.imshow("Publisher Frame", image)
        cv2.waitKey(10000)
        rospy.loginfo("End Publishingh image")
    except CvBridgeError as e:
        print(e)
    rate.sleep()

    
    
  