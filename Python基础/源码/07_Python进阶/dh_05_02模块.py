title = "猫模块"


def sayhello():
    print("小猫也会打招呼")


class Cat(object):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("%s 在喵喵叫" % self.name)
