
title = "毛毛"


def sayhello():
    print("Cat hello world")


class Cat(object):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("%s 喵喵叫" % self.name)
