import requests

url = "http://10.98.225.184:8084/mw/api/getcontentinfo?id=000621835&type=2"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

print(type(response))
response(status)
