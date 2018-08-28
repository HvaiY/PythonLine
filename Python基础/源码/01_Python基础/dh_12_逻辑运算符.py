# 与 and /  或 or / 非 not 三种逻辑判断
# 数字不小于18
num = 18
if not num < 18:
    print("数字不小于18")

# 年龄 在 0 -120 之间
if 0 <= num <= 120:  # 非简化写法 num>=0 and num <=120:
    print("年龄正常")
else:
    print("你不是人类")

# 只要一个成绩大于 60就通过

python_score = 80
c_score = 50
if python_score > 60 or c_score > 60:
    print("通过考试")
else:
    print("failed,补考吧")
