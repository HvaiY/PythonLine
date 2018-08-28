#  继承是为了代码的重用
# 父类 派生类


class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def sleep(self):
        print("睡")

    def run(self):
        print("运动")


# 子类继承
class Dog(Animal):
    pass


wc = Dog()
wc.eat()
wc.drink()
wc.run()
wc.sleep()
