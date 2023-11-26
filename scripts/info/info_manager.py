from geometry_msgs.msg import Twist
import rospy
import json
from config import config


def log_printer(func):
    def new_func(_, val):
        rospy.logwarn(val)
        return func(_, val)
    return new_func


class infoManager:
    def __init__(self):
        # speed and angular control
        self.twist = Twist()
        # run mileage
        self.mileage = 0

    def get_linear_x(self):
        return self.twist.linear.x

    @log_printer
    def set_linear_x(self, val):
        self.twist.linear.x = val
        
    def add_linear_x(self):
        if self.twist.linear.x < config.MAX_SPEED:
            self.twist.linear.x += config.SPEED_STEP
    
    def sub_linear_x(self):
        if self.twist.linear.x > 0:
            self.twist.linear.x -= config.SPEED_STEP
            
    def add_angular_z(self):
        if self.twist.angular.z < config.MAX_ANGULAR:
            self.twist.angular.z += config.ANGULAR_STEP
            
    def sub_angular_z(self):
        if self.twist.angular.z > -config.MAX_ANGULAR:
            self.twist.angular.z -= config.ANGULAR_STEP

    def get_angular_z(self):
        return self.twist.angular.z

    def set_angular_z(self, val):
        self.twist.angular.z = val

    def get_twist(self):
        return self.twist

    def set_twist(self, val):
        self.twist = val

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, val):
        self.mileage = val

    def get_all(self):
        data = [{'mileage': self.mileage, 'speed': self.twist.linear.x, 'direct': self.twist.angular.z}]

    def stop(self):
        self.twist = Twist()


info_manager = infoManager()
