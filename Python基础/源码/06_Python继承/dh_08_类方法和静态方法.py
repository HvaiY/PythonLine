# 类方法
class Tool(object):
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量：%d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


Tool.show_tool_count()

# 创建工具对象
tool1 = Tool("笔记本")
tool2 = Tool("电脑")

# 调用类方法
Tool.show_tool_count()

print("*" * 50)


# 静态方法
class Dog(object):
    # 静态方法，不访问实例属性也不访问类属性就定义为静态方法 ，用@staticmethod标记，没有参数self
    @staticmethod
    def run():
        print("小狗跑了")


# 通过类名.调用静态方法
Dog.run()
