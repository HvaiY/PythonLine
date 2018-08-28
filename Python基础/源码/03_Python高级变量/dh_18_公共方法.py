# len(item)　del(item) max(item) min(item)（最大最小值在字典中比较的是key）
# cmp（item1,item2） 比较两者的大小　python3　没有这个函数，可以是用 > < =等
# 切片　也可以切片列表,元组，但字典不行

num_list = [1, 4, 6, 8, 9, 3]
print(num_list[2:3])

# 运算符的用法
# +
str1 = "hello"
str2 = "world"
str3 = str1 + str2
print(str3)

num2_list = [7, 5]
num3_list = num_list + num2_list
print(num3_list)

# *　不仅仅只用于字符串　还可以用于列表和元组　但是字典和int不行 ###################
num2_list = num2_list * 5
print(num2_list)

num_tuple = ("啊啊", 12, True) * 5
print(num_tuple)

# num_dic = {"name": "大海"} * 5  # 改操作无法实现
# print(num_dic)　
