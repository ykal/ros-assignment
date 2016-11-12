#!/usr/bin/env python
import rospy
from turtlesim.srv import TeleportAbsolute
import socket, pickle
import threading
import time

def move_turtle(x, y):
    print("moving the turtle")
    rospy.wait_for_service("/turtle1/teleport_absolute")
    try:
        teleop=rospy.ServiceProxy("/turtle1/teleport_absolute",TeleportAbsolute)
        teleop(x,y,0)
        print("moved")
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


def start_client():
    move_turtle(4,4)
    host = "127.0.0.1"
    port = 6002
    client = socket.socket()
    try:
        client.connect((host, port));
        print("connected to the server")
    except Exception as e:
        print("Server is Down")

    while not rospy.is_shutdown():
        try:
            data_str = client.recv(4096)
            print(data_str)       
            data = data_str.split("|")
            print("start movving")
            rospy.wait_for_service("/turtle1/teleport_absolute")
            try:
                teleop=rospy.ServiceProxy("/turtle1/teleport_absolute",TeleportAbsolute)
                teleop(float(data[0]), float(data[1]), 0)
                print("moved")
            except rospy.ServiceException, e:
                print "Service call failed: %s"%e
        except Exception as e:
            pass

if __name__ == "__main__":
    rospy.init_node("turtle_client_node", anonymous=False)
    start_client()


    #  if data_str:
    #             prit("data_str")
    #             # data=data_str.split("|")
    #             # move_turtle(int(data[0]), int(data[1]))
    #             # print(type(data_str))
    #             print("data recived")