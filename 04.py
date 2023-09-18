import requests

tunnel = ""

# 用户名密码方式
username = ""
password = ""
proxy = {
    "http": ""
}

url = "http://www.cheshi.com/"
url_ip = "182.34.26.49"
res = requests.get(url_ip, proxies=proxy)
print(res.text)