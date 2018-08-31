name = "小明"


def say_hello():  # 函数定义 函数的上方需要有两空白行
    """打招呼"""

    print("你好，世界")
    print("hello world")
    print("你好，Python")


print(name)
say_hello()  # 函数调用 主动调用才会执行函数 ctrl + q 可以直接看到函数的说明这是在PyChar里面有效
print(name)

#  注 因为Python是解释性语言，需要一行一行的解释执行，
#  因此需要先定义函数才能调用，在调用的代码之前定义好（C# 为编译语言，函数可以在类空间的任意位置）
