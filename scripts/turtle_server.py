#!/usr/bin/env python
import socket, pickle
import rospy
from geometry_msgs.msg import Twist
import math
prev_angle = math.degrees(0)
def adjust_data(data):
    x = float(data.linear.x)
    z = float(data.angular.z)

    if math.fabs(z) == 2.0:
        z = math.degrees(1.91986217719)
        if z < 0:
            z = z + math.degrees(math.pi)
        global prev_angle
        prev_angle = z
    elif z == 0.0:
        z = 0

    loc_x = x * math.cos(prev_angle)
    loc_y = x * math.sin(prev_angle)

    return [loc_x, loc_y]

    print("----------------------------")
    print(prev_angle)
    print(loc_x)
    print(loc_y)
    print("----------------------------")

def callback(data):
    data = adjust_data(data)
    data_string = pickle.dumps(data)
    c.send(data_string)
    print("data has been sent")
    print(data)
    


def start_server():
    host = "127.0.0.1"
    global port
    port = 5055

    server = socket.socket()
    server.bind((host, port))
    


    server.listen(1)
    global c
    global d
    c, add = server.accept();
    print("Client Connected")


if __name__ == "__main__":
    start_server()
    rospy.init_node("cmd_vel_subscriber", anonymous=False)
    subscriber = rospy.Subscriber("/turtle1/cmd_vel", Twist, callback)
    rospy.spin()
    