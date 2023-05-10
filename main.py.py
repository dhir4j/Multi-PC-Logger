import os
import psutil
import platform
import json
import requests
import time
import socket

SERVER_URL = 'http://localhost:8000/pclogger/add_pc_info/'

def get_system_info():
    system_info = {}
    system_info['os'] = platform.system()
    system_info['version'] = platform.version()
    system_info['ram'] = round(psutil.virtual_memory().total / (1024 ** 3), 2) # convert to GB and round to 2 decimal places
    system_info['hdd'] = round(psutil.disk_usage('/').total / (1024 ** 3), 2)
    system_info['ip_address'] = socket.gethostbyname(socket.gethostname())
    return system_info

def send_to_server():
    with open('system_info.txt', 'r') as f:
        data = f.readlines()
        data = [json.loads(d) for d in data]
        for d in data:
            requests.post(SERVER_URL, json=d)

if __name__ == '__main__':
    while True:
        system_info = get_system_info()
        with open('system_info.txt', 'a') as f:
            f.write(json.dumps(system_info) + '\n')
        # if os.path.getsize('system_info.txt') > 10_000_000: # check if file size is greater than 10 MB
        send_to_server()
        os.remove('system_info.txt')
        time.sleep(15*60)  # send data every 15 minutes
