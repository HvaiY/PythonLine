# 模块的引入和重名
import dh_05_01模块 as DogModule
import dh_05_02模块 as CatModule

# 使用模块
DogModule.sayhello()
CatModule.sayhello()

wc = DogModule.Dog("旺财") # 对象
wc.bark()

tom = CatModule.Cat("tom")
tom.bark()

