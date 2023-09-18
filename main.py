import requests

# 1 直接获取网页源码
# url = 'http://www.cheshi.com'
# res = requests.get(url)
# print(res.encoding)
#
# with open("./cp01/index.html", "a") as f:
#     f.write(res.text)

# 2 获取图片
url_img = "https://media.cheshi-img.com/202308/64dec8a88a27c.jpg"
res_img = requests.get(url_img)
# 这是编码后的文字
# print(res_img.text)
# 这才代表二进制数据
print(res_img.content)
with open("./cp01/img.jpg", "a") as f:
    f.write(res_img.content)
