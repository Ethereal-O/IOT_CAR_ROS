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
    #     threading.Thread(target=self.report).start()

    # def report(self):
    #     while True:
    #         if not (self.running):
    #             continue
    #         self.send_message(info_manager.get_all())
    #         time.sleep(config.SLEEP_TIME)

    def recv_msg(self, request_id, command):
        # while self.running:
        #     recv_data = self.fd.readline()
        #     info_manager.set_linear_x(float(recv_data) / config.SPEED_SCALE)
        print(('Command, device id:  ', command.device_id))
        print(('Command, service id = ', command.service_id))
        print(('Command, command name: ', command.command_name))
        print(('Command. paras: ', command.paras))
        self.iot_client.respond_command(request_id, result_code=0)
        print('------------------this is myself callback')

    def send_message(self, message):
        self.fd.write(str(message) + config.END_FLAG)
        self.fd.flush()