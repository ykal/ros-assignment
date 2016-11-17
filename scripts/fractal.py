#!/usr/bin/env python
import rospy
import math
from turtlesim.srv import TeleportAbsolute
from std_srvs.srv import Empty
from turtlesim.srv import SetPen

teleop = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute);
setpen = rospy.ServiceProxy('/turtle1/set_pen', SetPen)
clear = rospy.ServiceProxy('/clear', Empty)

r = int(rospy.get_param("background_r"))
g = int(rospy.get_param("background_g"))
b = int(rospy.get_param("background_b"))

def draw_fractal(x, y, size):
    setpen(0,255,0,4,0)
    original_x = x #= x+1
    teleop(0,0,0)
    teleop(x, y, 0)
    clear()
    teleop(x+size, y, 0)
    teleop((x+size/2), -(size * math.sin(math.degrees(math.pi / 3))), 0)
    teleop(x, y, 0)
    setpen(r,g,b,4,0)

    for i in range(6):
        x = x + 2
        teleop(x, y, 0)
        setpen(0,255,0,4,0)
        teleop(x+size, y, 0)
        teleop((x+size/2), -(size * math.sin(math.degrees(math.pi / 3))), 0)
        teleop(x, y, 0)
        setpen(r,g,b,4,0)
    for d in range(4):
        y+=0.5
        x = original_x - 2
        for i in range(7):
            x = x + 2
            teleop(x, y, 0)
            setpen(0,255,0,1,0)
            teleop(x+size, y, 0)
            teleop((x+size/2), (size * math.sin(math.degrees(math.pi / 3))), 0)
            teleop(x, y, 0)
            setpen(r,g,b,1,0)
    y = y+1
    x = original_x
    teleop(x, y, 0)
    for i in range(6):
        x = x + 2
        teleop(x, y, 0)
        setpen(0,255,0,4,0)
        teleop(x+size, y, 0)
        teleop((x+size/2), -(size * math.sin(math.degrees(math.pi / 3))), 0)
        teleop(x, y, 0)
        setpen(r,g,b,4,0)
    for d in range(4):
        y+=0.5
        x = original_x - 2
        for i in range(7):
            x = x + 2
            teleop(x, y, 0)
            setpen(0,255,0,1,0)
            teleop(x+size, y, 0)
            teleop((x+size/2), (size * math.sin(math.degrees(math.pi / 3))), 0)
            teleop(x, y, 0)
            setpen(r,g,b,1,0)
    

        



# test(0)
draw_fractal(0,0, 0.5)
