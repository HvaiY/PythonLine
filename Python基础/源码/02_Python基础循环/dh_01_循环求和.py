# 求1-100的偶数和

i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1
print("1-100的偶数和为：%d" % result)

# 关键字 break 退出当前循环 不再执行后续的重复的代码
# 跳出循环之后 就是终止循环了

j = 0
while j <= 10:
    if j == 5:
        break

    print(j)
    j += 1

print("over")

# continue 满足某一条件之后 不在执行后续的重复代码， 不退出循环
# 直接跳到循环的判断条件中
n = 0
while n <= 10:
    if n == 5:
        # 注意要+1 不然会导致死循环了 后面打印n就没有了
        n += 1
        continue

    print(n)
    n += 1

print("over")

x3 = 0
while x3 < 10:
    if x3 == 8:
        break
    if x3 == 3:
        x3 += 1
        continue
    x3 += 1
    print(x3)

print("Over")
