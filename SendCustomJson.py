import requests
r = requests.post('http://localhost:8000/pclogger/add_pc_info/', json={"os": "Windows", "version": "10.0.22621", "ram": 7.35, "hdd": 476.08, "ip_address": "192.168.0.192"})
print(f"Status Code: {r.status_code}, Response Content: {r.content}")
