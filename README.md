# JSON REST Data server

Fast JSON RESTful server. Simple tool for stashing and fetching JSON data on the network. Built for speed and simplicity with just a bit of security.
Think of it as an alternative to a small database or a small data lake. Great for keeping track of inventory items or machine learning data.
This is an Agile project currently in MVP status (Minimum Viable Product)

# Setup

- Create `data/tokens.json` using the below example
- Test using `test_post.py`
- Tokens enable RBAC (role-based access control)
- This prevents any random person from reading or overwriting your data

Example tokens file:
```json
[
{"token": "readonlypassword", "role": "readonly"},
{"token": "supersecretpassword", "role": "readwrite"}
]
```

# Fetching data

Note: file extension is not required (I like to keep it nice and clean)

- Run a `GET` against the API with the endpoint being the filename with or without the JSON file extension
- The server will automatically append the JSON file extension for you for simplicity and cleanliness
- `verify=False` is for SSL certificate 
- `headers=headers` is for conveying the token for RBAC authentication

```python
headers = {'token': 'readonlypassword'}
r = requests.get("https://localhost/json_file", headers=headers, verify=False)
print('GET result:', r.text)
```

# Uploading data

- Payload needs to be JSON serializable
- The data needs to be in a string format, not binary
- API endpoint is `/new/`


```python
payload = {'time': str(datetime.now())}
headers = {'token': 'supersecretpassword'}
print('PAYLOAD to send:', payload)
r = requests.post("https://localhost/new/json_file", json=payload, headers=headers, verify=False)
print('POST result:', r.text)
```

# View all available files

- readonly privilege required
- enumerates all JSON files under `/data/`

```python
headers = {'token': 'readonlypassword'}
r = requests.get("https://localhost/", headers=headers, verify=False)
print('GET result:', r.text)
```