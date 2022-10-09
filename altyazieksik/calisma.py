import requests
import json
import re
url = "https://itvepg10013.tmp.tivibu.com.tr/iptvepg/frame3046/sdk_getvodurl.jsp?programcode=0000000030010000006973&columncode=02040001&urlredirect=1"

payload = ""
headers = {
  'Cookie': 'JSESSIONID=53E64E57F1D8ECAC96EE4943D5C0B696; JSESSIONID=DB8A80B2E480716F2E80B055BD70F048; TS0197d1e1=012845365a5ecec3320733d5a8b52dad605c83db82823b5fd222a91f55795d25d96769f7937eea3faac2d4760837d4f30fd0cab1d3137e5a355eae803cca1115c6045172cb; TS011688e6=012845365a4570a6a882214bdde8d7bce025736171a965976528f2ef7d22893549528481d1a4ca6b7c29e17fc683157462454aacaa'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# json_data=json.loads(response.text)
#print(json_data)
# for attr in json_data :
#     print(attr['playurl'])

cdnurl=re.search(r'(?<="httpsplayurl":")(.*)(?=","returncode")',str(response.text))
#print(cdnurl.group(1))

#print(type(cdnurl))
#print(cdnurl)
#
# #
 url = '{}'.format(str(cndurl.group(1)))

 print(url)
# payload={}
# headers = {
#   'Cookie': 'JSESSIONID=53E64E57F1D8ECAC96EE4943D5C0B696'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)
