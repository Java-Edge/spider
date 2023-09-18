import requests

url = 'https://product.cheshi.com/rank/2-0-0-0-1/'
res = requests.get(url)
# print(res.text)
print(res.request.headers)

with open("./cp01/index.html", "a") as f:
    f.write(res.text)
