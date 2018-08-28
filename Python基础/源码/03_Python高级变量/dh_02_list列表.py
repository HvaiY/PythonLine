# list 列表：用来存储多个数据　(可以是数字型 也可以是非数字型)　在其它语言中　对应的是数组
names_list = ["张三", "李四", "王五", "赵六", "钱七", "孙八"]

counts = names_list.__len__()
print(counts)
n = 0
while n < counts:
    print(names_list[n])
    n += 1
print("")

#  1.list　的取值和取索引
print(names_list[3])
# 　获取李四所在的索引的位置
print(names_list.index("李四"))
#  2.修改
names_list[3] = "大海"
# 增加
names_list.append("dahai")  # 在列表的后面追加数据
names_list.insert(2, "小丫丫")  # 在列表中指定的索引插入数据
temp_list = ["孙悟空", "猪哥"]

names_list.extend(temp_list)  # 将其它列表追加到该列表中
# 删除
name = names_list.pop()  # pop不带参数就删除列表的最后一个元素，带参数就是删除索引的元素，并返回元素
print(name)

names_list.remove("李四")  # 删除指定元素

names_list.insert(2, 33)
# names_list.clear()  # 清空列表
print(names_list)
