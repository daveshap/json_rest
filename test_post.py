import requests
from datetime import datetime


payload = {'time': str(datetime.now())}
print(payload)
r = requests.post("http://localhost/new/new.json", json=payload)
print(r.text)