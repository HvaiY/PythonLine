# if 进阶 elif

# 评估成绩级别
score = int(input("请输入成绩："))
if (score <= 100) and (score > 90):
    print("优")
elif score > 70:
    print("良")
elif score > 60:
    print("及格")
else:
    print("差")
print("OK 完毕")

# 选中一段代码可以使用 tab 进行缩进

# 嵌套if
if score > 60:
    print("成绩及格了")
    if score > 90:
        print("可以得到奖学金了")
    else:
        print("无缘奖学金")
else:
    print("好好学习吧")
