# encoding:utf-8

import base64

'''
通用文字识别（高精度版）
'''

import requests

url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=KNQUOpA0gn7qX4eUOIkDRlPW&client_secret=Drmtxj4GLKyOboLgsdxYZ1rUkj4UCqzB"

payload = ""
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

access_token = response.json()["access_token"]

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
f = open('./img/validate.png', 'rb')
img = base64.b64encode(f.read())

params = {"image": img}
access_token = access_token
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json()["words_result"][0]["words"])
