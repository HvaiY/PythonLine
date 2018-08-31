# 文字居中对其
poem = ["登黄鹤楼",
        "王焕之",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for str in poem:
    print("|%s|" % str.center(10, "　"))

# 左边对齐
for str1 in poem:
    print("|%s|" % str1.ljust(10, "　"))

# 右边对齐
for str2 in poem:
    print("|%s|" % str2.rjust(10, "　"))
print("*" * 50)

poem1 = ["\r\n登黄鹤楼",
         "王焕之",
         "白日依山尽",
         "黄河入海流\r\n",
         "欲穷千里目",
         "更上一层楼"]
for str3 in poem:
    # 去除两边空格　还有ltrip 和ｒtrip　
    print("|%s|" % str3.strip().center(10, "　"))
# 拆分　与合并
poem_str = '登黄鹤楼 王焕之 白日依山尽 黄河入海流 欲穷千里目 更上一层楼'
poem_list = poem_str.split(' ')  # 分割字符串成为　list  列表

print(poem_list)

# 合并 将‘－’合并到列表中，返回一个字符串
poem_ss = "-".join(poem_list)
print(poem_ss)

# 字符串切片　也就是截取一段
num_str = "０１２３４５６７８９"
print(num_str[2:6])  # 从第二个位置开始　切到第五个位置
print(num_str[:5])  # 切出前面五个字符
print(num_str[:])  # 切出所有字符
print(num_str[::2])  # 隔一个切一个
print(num_str[1::2])  # 隔一个切一个 从１开始到最后隔一个切一个
print("@"*100)
print(num_str[:-1])  # 倒序是－１ 开始　这里是从０切到倒数第二个
print(num_str[2:-3])  # 第二个位置开始　到－３位置结束切
print(num_str[::-1])  # 隔　－１隔切一个　形成倒序的效果