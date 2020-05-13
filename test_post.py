import requests
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# POST example
payload = {'time': str(datetime.now())}
headers = {'token': 'supersecretpassword'}
print('PAYLOAD to send:', payload)
r = requests.post("https://localhost/new/new.json", json=payload, headers=headers, verify=False)
print('POST result:', r.text)


# GET example
headers = {'token': 'readonlypassword'}
r = requests.get("https://localhost/new.json", headers=headers, verify=False)
print('GET result:', r.text)


# view files example
headers = {'token': 'readonlypassword'}
r = requests.get("https://localhost/", headers=headers, verify=False)
print('GET result:', r.text)
