# JSON REST server

Fast JSON RESTful server. Simple tool for stashing and fetching JSON data on the network. 

# Setup

- Create `data/tokens.json` using the below example
- Test using `test_post.py`

Example tokens file:
```json
[
{"token": "readonlypassword", "role": "readonly"},
{"token": "supersecretpassword", "role": "readwrite"}
]
```

# Fetching data

Note: file extension is not required (I like to keep it nice and clean)

```python
headers = {'token': 'readonlypassword'}
r = requests.get("https://localhost/json_file", headers=headers, verify=False)
print('GET result:', r.text)
```

# Uploading data

```python
payload = {'time': str(datetime.now())}
headers = {'token': 'supersecretpassword'}
print('PAYLOAD to send:', payload)
r = requests.post("https://localhost/new/json_file", json=payload, headers=headers, verify=False)
print('POST result:', r.text)
```

# View all available files

```python
headers = {'token': 'readonlypassword'}
r = requests.get("https://localhost/", headers=headers, verify=False)
print('GET result:', r.text)
```