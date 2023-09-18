import requests
from lxml import etree

url = 'https://product.cheshi.com/rank/2-0-0-0-1/'

headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


def parse(url):
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.text)
    items = tree.xpath('//div[@class="rank-modules-works"]//div[@class="rank-modules-works--main-item-content"]')
    for item in items:
        print(item)


if __name__ == '__main__':
    parse("https://www.zongheng.com/rank?nav=one-day&rankType=3")