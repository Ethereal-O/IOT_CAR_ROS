from info.info_manager import info_manager
import threading
import time
from geometry_msgs.msg import Twist
import rospy
from config import config
from sockets import sockets
import random


class scheduler:
    def __init__(self):
        self.cmd_vel_pub = rospy.Publisher("~cmd_vel", Twist, queue_size=1)
        self.tcp_client = sockets.sockets()

    def publish_twist(self):
        twist = info_manager.get_twist()
        if not twist:
            twist = Twist()
        self.cmd_vel_pub.publish(twist)

    def single_publish(self):
        while (True):
            self.publish_twist()
            time.sleep(config.SLEEP_TIME)

    def start_continue_publish(self):
        threading.Thread(target=self.single_publish).start()
    
    def start_socket(self):
        self.tcp_client.start()

    def start_all(self):
        # start changing paramter
        self.start_continue_publish()
        # start socket client
        self.start_socket()
