import requests
import json
import re
from xml.etree import ElementTree as ET


url = "https://itvepg10013.tmp.tivibu.com.tr/iptvepg/frame3046/sdk_getvodurl.jsp?programcode=0000000030010000629003&columncode=02040001&urlredirect=1"

payload={}
headers = {
  'Cookie': 'JSESSIONID=5F7C12578CE465146D879B928B2ABE64; TS011688e6=012845365aa9e7c9bc9e0497c5d126fdd3f2edc85dd2c7ec8b89fed237a829ade007e3b5c416d0d208c67d2772a78a3f36410d531d'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)

#json_data = json.loads(response.text)

#print(json_data)

# for attr in json_data:
#     print(attr)

tree=ET.parse(response.text)
root=tree.getroot()
print(root)

with

for x in root.findall('playurl'):
    #print(x.attrib['playurl'])

    print(re.search(r'playurl:\.(.*?)breakpoint',x))
