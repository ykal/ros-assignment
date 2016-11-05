#!/usr/bin/env python
import rospy
from Tkinter import *
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse
import random
import math

class Application(Frame):

    def createWidgets(self):
        self.frame1 = Frame(self)

        self.upButton = Button(self.frame1)
        self.upButton["text"] = "^"
        self.upButton["command"] =  self.upArrowCommand
        self.upButton.grid(row=0, column=1)

        self.leftButton = Button(self.frame1)
        self.leftButton["text"] = "<"
        self.leftButton["command"] =  self.leftArrowCommand
        self.leftButton.grid(row=1, column=0)

        self.rightButton = Button(self.frame1)
        self.rightButton["text"] = ">"
        self.rightButton["command"] =  self.rightArrowCommand
        self.rightButton.grid(row=1, column=2)

        self.downButton = Button(self.frame1)
        self.downButton["text"] = "v"
        self.downButton["command"] =  self.downArrowCommand
        self.downButton.grid(row = 2, column = 1)
        
        self.frame1.grid(row = 2, column = 2, padx = 10, pady = 10)
        
        self.frame2 = Frame(self)

        self.change_color = Button(self.frame2)
        self.change_color["text"] = "Change Colors"
        self.change_color["command"] =  self.showPopup
        self.change_color.grid(row = 0, column=1, padx = 5, pady = 5)


        self.clear = Button(self.frame2)
        self.clear["text"] = "Clear"
        self.clear["command"] =  self.clearCommand
        self.clear.grid(row = 2, column = 0, padx = 5, pady = 5)

        self.Quit = Button(self.frame2)
        self.Quit["text"] = "Quit"
        self.Quit["command"] =  self.exitCommand
        self.Quit.grid(row = 2, column = 2, padx = 5, pady = 5)

        self.frame2.grid(row = 2, column = 4, padx = 10, pady = 10)

    def showPopup(self):
        self.popup = Toplevel()
        
        self.frame3 = Frame(self.popup)

        self.lable_r = Label(self.frame3)
        self.lable_r["text"] = "background_r : "
        self.lable_r.grid(row = 0)

        self.entry_r = Entry(self.frame3)
        self.entry_r.grid(row = 0, column = 2)

        self.lable_b = Label(self.frame3)
        self.lable_b["text"] = "background_b : "
        self.lable_b.grid(row = 1, column = 0)

        self.entry_b = Entry(self.frame3)
        self.entry_b.grid(row = 1, column = 2)
        
        self.lable_g = Label(self.frame3)
        self.lable_g["text"] = "background_g : "
        self.lable_g.grid(row = 2, column = 0)

        self.entry_g = Entry(self.frame3)
        self.entry_g.grid(row = 2, column = 2)

        self.change = Button(self.frame3)
        self.change["text"] = "Change"
        self.change.grid(row = 5, column = 1)
        self.change["command"] = self.change_bg

        self.frame3.grid(row = 0, column = 0, padx = 20, pady = 20)

        self.popup.transient(self.master)
        self.popup.grab_set()
        self.master.wait_window(self.popup)
    def clearCommand(self):
        print("calling clear service")
        bg_clear = rospy.ServiceProxy('clear', Empty)
        success = bg_clear.call();
        if(success):
            print("Cleared")
        else:
            print("Error, something is wrong.")


    def exitCommand(self):
        print("exiting")
        self.master.destroy()
    def upArrowCommand(self):
        motion = Twist()
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=2)
        rate = rospy.Rate(10)
        if not rospy.is_shutdown():
            motion.linear.x = 2
            pub.publish(motion)
    
    def leftArrowCommand(self):
        motion = Twist()
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=2)
        rate = rospy.Rate(10)
        if not rospy.is_shutdown():
            motion.angular.z = 2
            pub.publish(motion)

    def downArrowCommand(self):
        motion = Twist()
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=2)
        rate = rospy.Rate(10)
        if not rospy.is_shutdown():
            motion.linear.x = -2
            pub.publish(motion)
    
    def rightArrowCommand(self):
        motion = Twist()
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=2)
        rate = rospy.Rate(10)
        if not rospy.is_shutdown():
            motion.angular.z = -2
            pub.publish(motion)

    
  
  
    def change_bg(self):

        if self.entry_b.get() == "":
            rospy.set_param("background_b", 0)
        else:
            rospy.set_param("background_b", int(self.entry_b.get()))
        if self.entry_g.get() == "":
            rospy.set_param("background_g", 0)
        else:
            rospy.set_param("background_g", int(self.entry_g.get()))
        if self.entry_r.get() == "":
            rospy.set_param("background_r", 0)
        else:
            rospy.set_param("background_r", int(self.entry_r.get()))
        
        self.clearCommand()   
        self.popup.destroy()
    
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
rospy.init_node('control_node', anonymous=False)
app = Application(master=root)
app.mainloop()
root.destroy()