class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("初始化发方法%s" % new_name)

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def __del__(self):
        print("%s 被销毁了" % self.name)


tom = Cat("Tom")  # 在创建对象的时候就自动调用了初始化方法__init__（）,
print(tom.name)

print("*" * 50)

del tom
print("对象被del 时也就是被销毁了，那么自动调用方法__del__()" * 1)
