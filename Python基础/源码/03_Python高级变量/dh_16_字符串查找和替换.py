hello_str = "hello world"
# 　判断是否以指定的字符串开始
print(hello_str.startswith("hello"))
# 　判断是否以指定的字符串结束
print(hello_str.endswith("ld"))
# 　查找指定字符串 所在的位置　，如果未找到返回－１
print(hello_str.find("llo"))

# 替换字符串 replace 返回的是一个替换后的字符串　，不修改原有的字符串
print(hello_str.replace("world", "python"))
print(hello_str)

print(hello_str.rindex("l"))  # 从右边开始查找索引位置
