def print_info(name, gender=True):
    """   根据条件打印参数name
      设置缺省参数一般是常见的，大多是是常用值
      1 给这个值指定一个默认值就可以了  调用的时候可以不指定，那么就是使用默认值了
      2缺省参数在函数的参数位置为参数的后面几位或者最后一位
      3 可以有多个缺省参数  ，调用的时候多个缺省参数需要明确指定
    :param name:  姓名
    :param gender:  True 男生，False 女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s是%s" % (name, gender_text))


# 不指定就是用默认值
print_info("小明")
# 指定就是用参数值
print_info("小明", gender=False)

print_info("小明", False) # 缺省值可以不用明确指定，但是出现多个缺省值 那么一定要明确指定
