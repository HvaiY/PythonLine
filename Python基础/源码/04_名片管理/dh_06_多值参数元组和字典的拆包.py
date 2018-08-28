def demo(*args, **kwargs):
    print(args)
    print(kwargs)


# 参数传递的时候我们使用参数的引用，需要加上* 和**就是拆包
num_args = ("1", 2, 4)
num_dic = {"name": "大海"}
# 查看一下结果就知道
demo(num_args, num_dic)

demo(*num_args, **num_dic)
