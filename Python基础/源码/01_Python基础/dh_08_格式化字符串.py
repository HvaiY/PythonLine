"""
格式化字符串
 %d 表示 十进制数字  %06d 十进制数字 自动补全
 %s 表示字符串
 %f 表示 浮点数字  %.2f 表示两位浮点数字  %.3f 等等
 %% 输出%

"""

name = "大海"

print("are name %s" % name)

print("---------------------")

num = 23

print("学号是 %d" % num)
print("学号是 %0d" % (num-3.3))  # 自动补全

price = 8.5
weight = 7.5
money = price * weight

print("苹果单价 %.2f ,数量是 %.3f ,金额是：%.4f" % (price, weight, money))

print("----------------------")

# 输出10%

scale = 0.8
print("占用总数的 %.2f%%" % (scale * 100))

print("%s价格是：%.2f 折扣为 %.2f%% 到手需花费%.2f" % ("苹果", 2, 7, 1.4))
