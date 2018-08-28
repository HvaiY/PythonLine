class Cat():
    # 如果外面没有属性name会报错，注意。
    def eat(self):
        print("%s 爱吃鱼" % self.name)


tom = Cat()
tom.name = "tom"
tom.eat()
