title = "狗模块"


def sayhello():
    print("狗狗也会打招呼")


class Dog(object):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("%s 在汪汪叫" % self.name)
