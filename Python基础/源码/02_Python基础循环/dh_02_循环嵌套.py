# 循环嵌套 打印小星星
num = 1
while num < 10:
    print("*" * num)
    num += 1

# 不使用字符串运算做到打印星星
row = 1

while row <= 10:
    col = 1
    while col <= row:
        print("*", end="")  # 不换行
        col += 1
    print("")  # 换行
    row += 1

# 乘法表
x = 1

while x <= 9:
    y = 1
    while y <= x:
        print("\t%d*%d=%d" % (y, x, x * y), end="")  # 不换行 python3才有这个
        y += 1
    print("")  # 换行
    x += 1
# 字符串中的转义字符
"""
\\ 反斜杠符号
\' 单引号
\" 双引号
\n 换行
\t 横向制表符  可以让字符串列对齐
\r 回车
"""
