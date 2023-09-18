import re

str = "X1Y22Y333Y444"

# 贪婪匹配（一直找到最后一个满足正则的字符）
# 所有X开头，Y结尾的子字符串
# ['X1Y22Y333Y']
# print(re.findall("X.*Y", str))

# 惰性匹配（一直找到最后一个满足正则的字符）
# ['X1Y']
# print(re.findall("X.*?Y", str))
# print(re.findall("\d.*?Y", str))


# str2 = "Hello World 123"
# exp = re.compile("\w+")
# # 匹配字符串中的所有单词，包括连续的单词和单个字符
# # ['Hello', 'World', '123']
# print(exp.findall(str2))



# 有时，我们只是匹配某些数据，但不想拿到
# str3 = "My name is JavaEdge!"
# "is" ：匹配 "is" 这个单词
# "(.*)" ：匹配任意数量的任意字符，并将其存储在一个组中
# "!" ：匹配感叹号
# 因此，这个正则表达式将匹配字符串中的 "is" 后面的单词和感叹号，并将这些单词存储在一个列表中
# exp = re.compile("is (.*)!")
# print(exp.findall(str3))

# str4 = "My name is JavaEdge!My name is GoogleEdge!My name is AIEdge!"
# "(.*?)" 匹配任意数量的任意字符，并将其存储在一个组中，使用 "?" 表示非捕获组，即不将其存储在匹配结果中
# exp = re.compile("is (.*?)!")
# print(exp.findall(str4))



str5 = """
My name is JavaEdge,and I am 18 years old.
My name is GoogleEdge, and I am 19 years old.
My name is AIEdge, and I am 20 years old.
"""

# "is" 表示匹配 "is" 这个单词
# "(.*?)" 表示匹配任意数量的任意字符，并将其存储在一个组中，使用 "?" 表示非捕获组，即不将其存储在匹配结果中
# "," 表示匹配逗号
# ".*?" 表示匹配任意数量的任意字符，使用 "?" 表示非捕获组，即不将其存储在匹配结果中
# "am" 表示匹配 "am" 这个单词
# "(\d*)" 表示匹配一个或多个数字，并将其存储在一个组中
# 因此，这个正则表达式将匹配字符串中的 "is" 后面的单词、逗号、空格和年龄，并将这些信息存储在一个列表中。
exp = re.compile("is (.*?),.*?am(\d*)")
for i, j in exp.findall(str5):
    # JavaEdge
    # GoogleEdge
    # AIEdge
    print(i, j)