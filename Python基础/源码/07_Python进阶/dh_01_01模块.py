title = "狗狗"


def sayhello():
    print("Dog hello world")


class Dog(object):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("%s 汪汪叫" % self.name)
