import requests

url = "http://127.0.0.1:5000/change_status"
data = {"intersection": "intersection_1", "status": "Green"}

response = requests.post(url, json=data)
print(response.json())
