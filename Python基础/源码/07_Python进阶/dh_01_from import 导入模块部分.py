# from ... import 引入模块的部分
from dh_01_01模块 import sayhello as DogMoudle_sayhello
from dh_01_02模块 import Cat
from dh_01_01模块 import sayhello

# 引入的部分模块调用， 显得很干净
# 注意，如果导入的部分模块的内容有相同方法或者属性的实惠，后面导入的会覆盖前面的
# 可以使用 as 重名导入的模块部分
DogMoudle_sayhello()
sayhello()
tom = Cat("tom")
tom.bark()
