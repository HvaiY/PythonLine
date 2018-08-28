def demo(num, *nums, **person):
    """多值参数
    当参数不确定的时候可以使用任意多值参数 多个参数
    * 元组 ** 字典
    :param num: 参数一
    :param nums: 元组参数
    :param person: 字典参数
    """
    print(num)
    print(nums)
    print(person)


demo(1)  # 第一个参数是1 后面的参数都是空的
demo(1, 2, 3, 4, 5)  # 第一个参数是 数字1，第二个参数是元组（2,3,4,5） 第三个参数是空

demo(1, 2, 3, 4, 5, name="小明")
# 第一个参数是1 后面元组参数是（2,3,4,5） 字典参数是{“name”:"小明"}


