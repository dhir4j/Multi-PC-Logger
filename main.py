import os
import psutil
import platform
import json
import requests
import time
import socket
# URL of the Django server endpoint
# SERVER_URL = 'http://localhost:8000/api/systems/'


def get_system_info():
    system_info = {}
    system_info['os'] = platform.system()
    system_info['version'] = platform.version()
    system_info['ram'] = round(psutil.virtual_memory().total / (1024 ** 3), 2) # convert to GB and round to 2 decimal places
    system_info['hdd'] = round(psutil.disk_usage('/').total / (1024 ** 3), 2)
    system_info['ip_address'] = socket.gethostbyname(socket.gethostname())
    return system_info


def save_to_text_file(system_info):
    with open('system_info.txt', 'a') as f:
        f.write(json.dumps(system_info) + '\n')


# def send_to_server():
#     with open('system_info.txt', 'r') as f:
#         data = f.readlines()
#         requests.post(SERVER_URL, json={'data': data})


if __name__ == '__main__':
    # while True:
    system_info = get_system_info()
    save_to_text_file(system_info)
    # send_to_server()
    # time.sleep(60)  # send data every minute

    # Print the location of the file
    print('System information is being saved in', os.path.abspath('system_info.txt'))
