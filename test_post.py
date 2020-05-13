import requests
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


payload = {'time': str(datetime.now())}
headers = {'token': 'supersecretpassword'}
print(payload)
r = requests.post("https://localhost/new/new.json", json=payload, headers=headers, verify=False)
print(r.text)