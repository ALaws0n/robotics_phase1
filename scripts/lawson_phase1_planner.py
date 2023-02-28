#!/usr/bin/env python3

import rospy
import math

# import the plan message
from ur5e_control.msg import Plan
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	# initialize the node
	rospy.init_node('lawson_phase1_planner', anonymous = True)
	# add publisher for joint position commands
	plan_pub = rospy.Publisher('/plan', Plan, queue_size = 10)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)
	# All angular velocities will stay the same
	angular_x = 3.14
	angular_y = 0.0
	angular_z = 1.57
	# Define a plan variable
	plan = Plan()
	plan_point1 = Twist()
	# define point close to init pos
	plan_point1.linear.x = -0.65
	plan_point1.linear.y = -0.133
	plan_point1.linear.z = 0.235
	plan_point1.angular.x = angular_x
	plan_point1.angular.y = angular_y
	plan_point1.angular.z = angular_z
	# add point to plan
	plan.points.append(plan_point1)
	
	plan_point2 = Twist()
	# define the pick up pos
	plan_point2.linear.x = -0.65
	plan_point2.linear.y = -0.133
	plan_point2.linear.z = 0.075
	plan_point2.angular.x = angular_x
	plan_point2.angular.y = angular_y
	plan_point2.angular.z = angular_z
	# add point to plan
	plan.points.append(plan_point2)
	
	plan_point3 = Twist()
	# define the safe waypoint pos
	plan_point3.linear.x = -0.78
	plan_point3.linear.y = -0.133
	plan_point3.linear.z = 0.235
	plan_point3.angular.x = angular_x
	plan_point3.angular.y = angular_y
	plan_point3.angular.z = angular_z
	# add point to plan
	plan.points.append(plan_point3)
	
	plan_point4 = Twist()
	# define the placement pos
	plan_point4.linear.x = -0.78
	plan_point4.linear.y = -0.133
	plan_point4.linear.z = 0.075
	plan_point4.angular.x = angular_x
	plan_point4.angular.y = angular_y
	plan_point4.angular.z = angular_z
	# add point to plan
	plan.points.append(plan_point4)
	
	while not rospy.is_shutdown():
		# publish the plan
		plan_pub.publish(plan)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
	
