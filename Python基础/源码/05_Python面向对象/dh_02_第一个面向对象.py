class Cat:
    """这是一个，猫类"""

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


tom = Cat()

# 如果需要增加属性 在Python中很简单，但是不推荐，属性应该是封装在对象内部的
tom.name = "小猫猫"
tom.drink()
tom.eat()

# 查看对象内存地址 16进制
print(tom)
# id方式
address = id(tom)
print(address)
# 16进制显示
print("%x" % address)
