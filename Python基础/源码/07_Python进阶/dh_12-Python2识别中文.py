# *-* coding:utf8 *-*

# Python 2x 使用的编码是ASCII
# Python 3X 默认使用的是UTF-8编码格式
# 为了让Python2识别中文 在程序的第一行加上 # *-* coding:utf8 *-*
str_hello = u"hello 世界"  # 小写字母u可以告知解释器这个是utf-8编码的
print(str_hello)

for c in str_hello:
    print(c)