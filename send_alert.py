import requests, json

url = "http://127.0.0.1:5000/alert/2113705847"

data = {"alert": "This is a cool message"}
json_data = json.dumps(data)

r = requests.post(url, json=json_data)