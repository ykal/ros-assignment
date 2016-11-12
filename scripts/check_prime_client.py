#!/usr/bin/env python
import rospy
import sys
from grey_scale.srv import *
import math

def client(x):
    rospy.wait_for_service('check_prime_service')

    try:
        # create a handle to the  service
        check_prime = rospy.ServiceProxy('check_prime_service', CheckPrime)
        resp1 = check_prime(x)
        return resp1.result
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    # get inputs 
    argv = rospy.myargv()

    if (len(argv) < 2) :
        print ("Usage : \n \tInsert integers Separeted By Space")
        sys.exit()

    args = []
    for i in argv:
        if i == argv[0]:
            pass
        elif i == " ":
            pass
           
        else:
            try:
                 args.append(int(i))
            except Exception, e:
                print("Please Insert approprate Input")
    x = args
    print("Arg : ")
    print (x)
    print("\n")
    print ("Result : ")
    print(client(x))
