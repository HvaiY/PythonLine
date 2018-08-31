import dh_05_01模块

print(dh_05_01模块)
# 对一个文件的操作 三步
# 1.打开文件（创建文件对象）//Pycharm中可以直接使用：file=open("dh_05_模块.py")
file = open("e:\\C#\\Python\\PythonLine\\Python基础\\源码\\07_Python进阶\\dh_05_模块.py")
# 2.读取文件
text = file.read()
print(text)
# 3.关闭文件，以便程序不再消耗系统资源，建议打开文件的时候同时写上关闭操作，以免忘记
file.close()

