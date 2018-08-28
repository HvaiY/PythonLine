class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("初始化发方法%s" % new_name)

    def __del__(self):
        print("%s 被销毁了" % self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "%s 小猫" % self.name


tom = Cat("Tom")
print(tom)  # 自动输出了小猫的字符串信息 相当C#的ToString()
