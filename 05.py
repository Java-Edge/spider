import re

import requests

url = "https://product.cheshi.com/rank/2-0-0-0-1/"
headers = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",

}
res = requests.get(url, headers=headers)

exp = re.compile('class="m_detail".*?href.*?>(.*?)<', re.S)

for title in exp.findall(res.text):
    print(title)