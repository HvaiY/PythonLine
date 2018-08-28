file = open("ReadMe")
# 2.读取文件
text = file.read()
print(text)

print("*"*50)
# 文件指针就是一个标记。上面默认读取到了文件的末尾，文件指针就移动到文档末尾
# 再次使用读取则没有数据了
text2 = file.read()
print(text2)
print(len(text2))
# 3.关闭文件，以便程序不再消耗系统资源，建议打开文件的时候同时写上关闭操作，以免忘记
file.close()