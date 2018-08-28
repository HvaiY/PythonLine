# 异常具备传递性，出现异常一层层向上抛出


def demo():
    num = int(input("请输入整数"))
    print(num)


def demo2():
    demo()


try:
    demo2()
except Exception as result:
    print("异常位置：%s" % result)
