names_list = ["张三", "赵六", "李四", "王五", "赵六", "钱七", "孙八"]
list_len = len(names_list)
print("列表中共有%d个元素" % list_len)
print("列表中共有%d个元素" % names_list.__len__())
count = names_list.count("赵六")

print("赵六在列表中出现了%d次" % count)

names_list.remove("赵六")  # 异常出现的第一个赵六 ctrl + q　看帮助文档

print(names_list)
