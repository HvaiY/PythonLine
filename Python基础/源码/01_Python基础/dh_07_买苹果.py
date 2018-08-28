price_str = input("请输入价格")
num_str = input("请输入数量")

price = float(price_str)
num = float(num_str)

money = price * num
print(money)

# 改进版本

print("---------------------")

p = float(input("请输入单价"))
w = float(input("请输入重量"))
m = p * w
print(m)
