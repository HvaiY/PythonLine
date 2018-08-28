#  面向对象三大特性： 封装，继承，多态
# 下面就是多态了


class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 愉快的玩" % self.name)


class XiaoTQ(Dog):
    def game(self):
        print("%s 飞到天上去玩撒" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和%s快乐的玩撒" % (self.name, dog.name))

        dog.game()  # 狗狗玩起来


# xtq = XiaoTQ("哮天犬")
xtq = XiaoTQ("旺财")  # 多态体现，狗变动就跟着变了
xiaom = Person("小明")
xiaom.game_with_dog(xtq)
