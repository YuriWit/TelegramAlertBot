import requests, json

url = "http://52.70.34.69/alert/2113705847"


# post
data = {"alert": "this is the message"}
json_data = json.dumps(data)
r = requests.post(url, json=json_data)
print(r.text)

# get
r = requests.get(url + "/?alert=nospacemessage")
print(r.text)
