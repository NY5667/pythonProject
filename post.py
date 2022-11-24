import requests

url = "http://aliv13.data.moji.com/whapi/json/aliweather/limit"

payload={'cityId': '1185',
'token': '50b53ff8dd7d9fa320d3d3ca32cf8ed1'}
files=[

]
headers = {
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Authorization': 'APPCODE 9de3803024934dd69757b185c2e66e7e'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
