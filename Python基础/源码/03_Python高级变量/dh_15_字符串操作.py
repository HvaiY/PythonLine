hello_str = "hello hello"

# 统计长度
print(len(hello_str))

# 　统计某一个小/子字符串出现的次数
print(hello_str.count("llo"))
print(hello_str.count("abc"))  # 结果是０

# 某一个子字符串出现的位置
print(hello_str.index("llo"))
# print(hello_str.index("lso"))  #找不到位置则报错　表示不存在子字符串

print("*" * 50)

# str_num = "1"
str_num = "一千六"
print(str_num.isdecimal())  # 全是数字返回true
print(str_num.isdigit())  # 全是数字 或者 \u00b2 返回true
print(str_num.isnumeric())  # 全是数字，汉字等，返回true
