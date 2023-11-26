from IoT_device.client.IoT_client_config import IoTClientConfig
from IoT_device.client.IoT_client import IotClient
import threading
import time
import rospy
from config import config
from info.info_manager import info_manager


class sockets:
    def __init__(self):
        self.client_cfg = IoTClientConfig(server_ip=config.SERVER_IP, device_id=config.DEVICE_ID, secret=config.SECRET, is_ssl=False)
        self.iot_client = IotClient(self.client_cfg)

    def __del__(self):
        self.running = False

    def start(self):
        self.iot_client.connect()
        self.iot_client.set_command_callback(self.recv_msg)
        self.running = True
        self.iot_client.start()
    
    def parse_command(self, command):
        print(('Command, device id:  ', command.device_id))
        print(('Command, service id: ', command.service_id))
        print(('Command, command name: ', command.command_name))
        real_command = None
        if config.COMMAND_KEY in command.paras
            real_command = command.paras[config.COMMAND_KEY]
        if real_command == "w":
            info_manager.add_linear_x()
        elif real_command == "s":
            info_manager.sub_linear_x()
        elif real_command == "a":
            info_manager.sub_angular_z()
        elif real_command == "d":
            info_manager.add_angular_z()
        elif:
            print("unknown command paras: ", command.paras)

    def recv_msg(self, request_id, command):
        self.parse_command(command)
        self.iot_client.respond_command(request_id, result_code=0)

    def send_message(self, message):
        self.fd.write(str(message) + config.END_FLAG)
        self.fd.flush()