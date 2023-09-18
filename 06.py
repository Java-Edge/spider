import re

str = "Hi \n _12"

# . 除了换行符之外的任意字符
# 匹配任意一个字符:匹配到了字符串中的每个字符
# print(re.findall(".", str))

# 匹配任意两个字符:结果是一个列表，包含了字符串中的所有连续两个字符
# print(re.findall("..", str))


# w 字母、数字、下划线
# ['H', 'i', '_', '1', '2']
# print(re.findall("\w", str))

# ['Hi', '_1']
# print(re.findall("\w\w", str))

# ['_12']
# print(re.findall("\w\w\w", str))
#
# W 非【字母、数字、下划线】
# [' ', '\n', ' ']
# print(re.findall("\W", str))




# d 仅数字
# ['1', '2']
# print(re.findall("\d", str))
# ['12']
# print(re.findall("\d\d", str))

# D 非数字
# ['H', 'i', ' ', '\n', ' ', '_']
# print(re.findall("\D", str))

# s 空格、换行符
# [' ', '\n', ' ']
# print(re.findall("\s", str))
# S 非【空格、换行符】
# ['H', 'i', '_', '1', '2']
# print(re.findall("\S", str))

# 组合使用
# ['\n _']
# print(re.findall("\s\s\w", str))

# 精准匹配字符
str2 = "Hello World 123"
# print(re.findall("e", str2))
# print(re.findall("ll", str2))
# print(re.findall("l\w", str2))


# 模糊匹配字符 包含一个字符即可
# ['d']
# print(re.findall("[abcd]", str2))
# ['1', '2']
# print(re.findall("[12]", str2))

# 模糊匹配字符 包含2个字符
# ['12']
# print(re.findall("[12][12]", str2))

# 示以数字1或2开头，后跟任意两个字符
# ['123']
# print(re.findall("[12]..", str2))

# 匹配任何小写字母a到f之间的字符
# ['e', 'd']
# print(re.findall("[a-f]", str2))


str3 = "122333 aabbcc"
# 匹配连续的三个数字
# ['122', '333']
# print(re.findall("\d{3}", str3))

# # 查找所有长度为3的连续字母数字字符
# ['122', '333', 'aab', 'bcc']
# print(re.findall("\w{3}", str3))



# * 0次或更多连续的字符
# 匹配连续出现的数字"1"（包括0次出现）
# ['1', '', '', '', '', '', '', '', '', '', '', '', '', ''] 因为把 2、3 都当做 1 出现 0 次的情况了，所以展示了空串
# print(re.findall("1*", str3))
# 连续出现的数字"1"，后跟一个"2"的子字符串
# ['12', '2']
# print(re.findall("1*2", str3))


# + 1次或更多连续的字符
# ['1']
# print(re.findall("1+", str3))

# ['122333', '', '', '', '', '', '', '', '']
# 查找所有连续的数字
# ['122333', '', '', '', '', '', '', '', ''] 直接匹配出符合规则的最长长度的字符串！！！
print(re.findall("\d*", str3))
