# 因为元组(tuple)不能被修改，但是列表(list)可以被修改，
# 我们可以将元组转为列表

# 元组
info_tuple = ("张三", 18, 1.75)
print(info_tuple)
# 转为列表
info_list = list(info_tuple)

# 修改数据
info_list[0] = "李四"

# 转为元组
info_tuple = tuple(info_list)

print(info_tuple)
