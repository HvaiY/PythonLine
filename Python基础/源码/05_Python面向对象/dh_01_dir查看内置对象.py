# dir 可以查看内置函数
# 在Python 中一切都是对象


def demo():
    """这是一个测试函数"""
    print("test")


demo()
print(dir(demo))
# 内置函数的结构是   __函数名__
# 调用内置函数 查看文档
print(demo.__doc__)

a=122
print(dir(a))