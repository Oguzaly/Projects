import requests
import json

url = "http://10.98.228.146:8090/contents"

payload = json.dumps({
  "contentType": "Film",
  "metadata": {
    "videoFormats": [
      "HD"
    ],
    "year": 2022
  },
  "name": "Test - yenitest",
  "type": "MOVIE"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
