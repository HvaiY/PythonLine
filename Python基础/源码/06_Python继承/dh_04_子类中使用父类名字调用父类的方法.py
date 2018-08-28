# 调用父类的方法 使用父类的名称，（这是2.0时候使用的，不推荐了，3.0用super）
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
        print("父类叫唤")


# 方法扩展： 关键字：super 当父类的方法不满足需求的时候重写父类的方法
class XiaoTianQuan(Animal):
    def bark(self):
        # 子类特有需求代码
        print("哮天犬像神一样叫")
        # # 使用super 调用父类的方法实现
        # super().bark()
        # 使用父类名的方式调用 ,不推荐了
        Animal.bark(self)

        # 其他需求
        print("瞎叫唤")


xtq = XiaoTianQuan()
xtq.bark()
