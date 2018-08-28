class A:
    def test(self):
        print("A test方法")


class B:
    def demo(self):
        print("demo 方法")

    def test(self):
        print("b test方法")


class C(A, B):  # 多继承 能够继承过来所有的方法和属性
    """多继承可以让子类同时具有多个父类的属性和方法"""

    pass


c = C()
c.test()
c.demo()
# 在多继承中，父类的方法和属性尽量不要相同，
# 不然阅读困难，并且容易不明确，
# 像上面的C类多继承， test方法的调用是先收索C 查找
# 找不到则找A ,A父类找不到就找父类B
# B父类找不到就找object,找不到就报错了。
print(C.__mro__)  # MRO收索顺序

print(dir(c))  # 查看c对象的方法(Python3中的类默认继承object，所以都是新式类)

print(2 ** 10)
