def measure():
    """测量温度和湿度"""
    print("测量开始")
    temp = 39
    wetness = 50
    print("测量结束")

    # 返回多个数据可以采用返回元组的方式
    # return (temp,wetness) # 元组括号可以不用有
    return temp, wetness


result = measure()

print(result)
print(result[1])
print(result[0])

# 以上从元组中拿数据比较麻烦 ，但是可以使用多个变量接受返回值
gl_temp, gl_wetness = measure()
# 注意 多个变量接受返回元组的函数的值需要注意变变量的数量和元组元素数量相同
print(gl_temp)
print(gl_wetness)
