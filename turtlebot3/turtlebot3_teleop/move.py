#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist

PI = 3.1415926535897


class movement:

    def __init__(self):
        rospy.init_node('move_robot_node', anonymous=False)
        self.pub_move = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

        self.move = Twist()

    def publish_vel(self):
        self.pub_move.publish(self.move)

    def move_forward(self):
        # print("hi")
        # move = Twist()
        self.move.linear.x = 1
        self.move.angular.z = 0.0
        # while not rospy.is_shutdown():
        # self.pub_move.publish(move)
        # self.rate.sleep()
        # print(Twist())

    def move_backward(self):
        # move = Twist()
        self.move.linear.x = -1
        self.move.angular.z = 0.0
        # self.pub_move.publish(move)

    def stop(self):
        # move = Twist()
        self.move.linear.x = 0
        self.move.angular.z = 0.0
        # self.pub_move.publish(move)

    def rotate_right(self):
        move = Twist()
        # Receiveing the user's input
        print("Let's rotate your robot")
        speed = 100
        angle = 90
        clockwise = True  # True or false

        # Converting from angles to radians
        angular_speed = speed*2*PI/360
        relative_angle = angle*2*PI/360

        # We wont use linear components
        move.linear.x = 0
        move.linear.y = 0
        move.linear.z = 0
        move.angular.x = 0
        move.angular.y = 0

        # Checking if our movement is CW or CCW
        if clockwise:
            move.angular.z = -abs(angular_speed)
            print(move.angular.z)
        else:
            move.angular.z = abs(angular_speed)
        # Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_angle = 0

        while(current_angle < relative_angle):
            self.pub_move.publish(move)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed*(t1-t0)
        # Forcing our robot to stop
        move.angular.z = 0
        # self.pub_move.publish(move)
        # rospy.spin()


if __name__ == "__main__":

    mov = movement()
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():

        direction = input("enter the direction: ")
        if direction == 'b':
            mov.move_backward()
        if direction == 'f':
            mov.move_forward()
        if direction == 's':
            mov.stop()
        if direction == 'rr':
            mov.rotate_right()
        mov.publish_vel()
        rate.sleep()
        # rospy.spin()
