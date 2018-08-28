class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18  # 私有属性和方法就是在方法命名前面增加两个下划线

    def secret(self):
        print("%s 的年龄是：%d" % (self.name, self.__age))


xiaoFang = Women("小芳")
# xiaoFang.__age  # 私有方法和属性是外部无法访问的，
xiaoFang.secret()
# 但是还是可以有方法访问私有属性和方法 对象._类名__私有方法属性名字
print("%d" % xiaoFang._Women__age)
