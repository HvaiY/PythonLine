# import 模块名字
# 如果模块的名字和和系统的模块名字相同的话 ，可能会导致系统的模块无法使用
# 在方法调用的时候 搜索模块才、是先搜索项目目录 然后在搜索系统目录，
# 可以使用  __file__查找模块定义的路径.
import random
# 使用* 可以导入模块所有工具 不建议使用
from dh_01_01模块 import *

print(title)
sayhello()
tom = Dog("tom")
tom.bark()

# num = random.randint(0,10)
# print(num)
# 查看模块文件路径
print(random.__file__)
