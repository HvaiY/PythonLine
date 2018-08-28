names_list = ["张三", "李四", "王五", "赵六", "钱七", "孙八"]

# del　关键字　本质是用来将一个变量从内存中删除
del names_list[1]
# del　删除了的变量　　后面就不能使用该变量了
print(names_list)

name = "大海";
print(name);
del name  # 被删的对象
