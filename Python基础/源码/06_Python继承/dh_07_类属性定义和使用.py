class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具数量，类属性通常用来记录跟类相关的特征 //C# 相当于静态属性
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


tool1 = Tool("笔记本")
tool2 = Tool("电脑")
tool3 = Tool("手机")

# 输出工具对象的总数 使用类名来访问类属性，当然获取属性还可以使用对象来获取，但是不推荐

print(Tool.count)

tool3.count = 99  # 这里并不是给类属性赋值，而是给对象tool3 创建了实例属性count
print(tool3.count)  # 这是是给对象tool3 添加了一个属性
print(tool1.count)  # 使用对象来获取类属性 ，不推荐
print(Tool.count)  # 类属性依然还是3
