# Tuple 元组　元素组成的序列，　可以存储不同的数据类型，
# 与列表不通　，元组定义后不能修改了
# 元组定义
empty_tuple = ()  # 定义空元组
empty_list = []  # 空列表
print(type(empty_list))
print(type(empty_tuple))

single_tuple = (5,)  # 定义包含一个元素的元组
print(type(single_tuple))

info_tuple = ("张三", 18, '男', 1.75, "李四", '男')

print(type(info_tuple))

# 按照索引获取元组数据
print(info_tuple[2])

for info in info_tuple:
    print(info)
print("*" * 50)
# 取元素和索引
print(info_tuple[3])
print(info_tuple.index("男"))
# 统计计数
print("出现男的次数是：%d" % info_tuple.count("男"))
print("info_tuple元组的长度是：%d" % len(info_tuple))

print(info_tuple.__len__())
print(info_tuple.__doc__)
