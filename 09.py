import requests
from lxml import etree

url = 'https://product.cheshi.com/rank/2-0-0-0-1/'

headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)
tree = etree.HTML(res.text)
print(tree)

items = tree.xpath('//div[@class="m_detail"]')
for item in items:
    title = item.xpath('.//a/text()')
    link = item.xpath('.//a/@href')
    price = item.xpath('.//b/text()')
    print(title, link, price)