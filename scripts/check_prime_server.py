#!/usr/bin/env python
import rospy
from grey_scale.srv import *
import math

def filter_prime_numbes(req):
    result = []
    for i in req.a:
        ceil_num = int(math.ceil(math.sqrt(i)) + 1);
        check = False


        if i == 1:
            result.append("None")
            continue

        if i == 2:
            result.append("T")
            continue
        for j in range(2, ceil_num):
            if i % j == 0:
                check = True
        if check:
            result.append("F")
        else :
            result.append("T")    

    return CheckPrimeResponse(result)

def server():
    rospy.init_node('check_prime_node', anonymous=False)
    srv = rospy.Service('check_prime_service', CheckPrime, filter_prime_numbes)
    rospy.spin()

if __name__ == "__main__":
    server();