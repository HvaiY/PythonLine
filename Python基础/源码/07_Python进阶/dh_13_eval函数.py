# eval函数 将字符串当当作代码执行
input_str = input("请输入算数题")

print(eval(input_str))

# 不要滥用eval函数

# 可以在控制台输入后面的命令看看效果： __import__('os').system('ls')

