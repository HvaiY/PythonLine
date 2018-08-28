# 格式化字符串%()　后面的()就是一个元组　，
# 元组应用场景还可以用于函数传参数
info_tuple = ("张三",18,'男')
print("%s 年龄是：%d 性别：%s" % info_tuple)

info_str="%s 年龄是：%d 性别：%s" % info_tuple
print(info_str)