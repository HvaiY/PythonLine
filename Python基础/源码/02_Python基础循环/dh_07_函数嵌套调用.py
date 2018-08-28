def test1():
    """打印×"""
    print("*" * 10)


def test2():
    """打印-"""
    print("-" * 10)
    # 函数嵌套调用
    test1()


test2()  # 调用函数
