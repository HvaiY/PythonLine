# 引入随机数包
import random

player = int(input("请输入1（石头），2（剪刀），3（布）："))

# random 中的函数 randint(10,20) 随机生成一个10-20d的数字

# 注意格式哦  包需要先引入，才是使用包里面的方法，和其他语言一样
computer = random.randint(1, 3)

print(computer)
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("腻害，你赢了")
elif player == computer:
    print("心有灵犀啊")
else:
    print("弱爆了，决战到天亮")
