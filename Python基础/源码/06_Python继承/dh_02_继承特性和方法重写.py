# 继承具有传递性
class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def sleep(self):
        print("睡")

    def run(self):
        print("运动")

    def bark(self):
        print("叫唤")

# 方法重写： 当父类的方法不满足需求的时候重写父类的方法
class XiaoTianQuan(Animal):
    def bark(self):
        print("哮天犬像神一样叫")

xtq = XiaoTianQuan()
xtq.bark()