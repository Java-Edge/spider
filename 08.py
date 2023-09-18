import requests
import re

headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


def parse_url(url):
    res = requests.get(url, headers=headers)
    res.encoding = "gb2312"

    # - '<td height="26">' 表示匹配一个 HTML 标签，包含 height 属性值为 "26" 的 td 标签
    # - '.*?' 匹配任意数量的任意字符，使用 "?" 表示非捕获组，即不将其存储在匹配结果中
    # - 'href="(.*?)"' 匹配一个 href 属性，其中包含了任意数量的任意字符，并将其存储在一个组
    # 匹配 HTML 文档中的所有包含 height 属性值为 "26" 的 td 标签，并提取其中 href 属性的值，存储在一个列表中
    # re.S 标志启用跨行匹配，即在正则表达式中使用换行符时，不将其解释为特殊字符。这样，就可以匹配到 HTML 标签中的换行符

    exp = re.compile('<td height="26">.*?href="(.*?)"', re.S)
    print(exp.findall(res.text))
    for link in exp.findall(res.text):
        link = "https://m.dytt8.net" + link
        parse_details(link)

    exp = re.compile("<a href='(.*?)'>下一页<")
    if len(exp.findall(res.text)) != 0:
        next_url = "https://btwuji.com/html/gndy/oumei/" + exp.findall(res.text)[0]
        print(next_url)
        parse_url(next_url)


def parse_details(url):
    res_details = requests.get(url, headers=headers)
    res_details.encoding = "gb2312"

    exp = re.compile('◎译　　名\u3000(.*?)<br />.*?◎年　　代\u3000(.*?)<br />◎产　　地\u3000(.*?)<', re.S)

    for title, year, country in exp.findall(res_details.text):
        print(title, year, country)


if __name__ == '__main__':
    parse_url("https://btwuji.com/html/gndy/oumei/index.html")
