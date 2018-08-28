# 九九乘法表 以下就是定义函数 def关键字 define :定义
def multiple_table():  # def 函数名称():
    x = 1
    while x <= 9:
        y = 1
        while y <= x:
            print("\t%d*%d=%d" % (y, x, x * y), end="")  # 不换行 python3才有这个
            y += 1
        print("")  # 换行
        x += 1
