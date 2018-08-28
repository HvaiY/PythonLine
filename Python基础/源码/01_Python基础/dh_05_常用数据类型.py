"""
姓名：小明
年龄：18
性别：男
身高：1.75米
体重：75.0
python  里面不需要指定数据类型 ，在运行的时候 解释器根据变量的值
来自动推导出变量中保存的数据类型
"""
name = "小明"
age = 18
gender = True
height = 1.75
weight = 75.0

print("我是："+name)

"""
复数型  complex ：主要是用于平面场问题，波动问题，
-------------------
数字型
int  long（python 没有long数据类型了）
bool
float True 真  也就是1   假 false 表示
---------------------
非数字型
 字符串
 列表
 元组
 字典
-------------------  
type 类型类型 可以获取数据的数据类型
"""
names = "dahai"
# 可以查看数据的数据类型
print(type(names))
# Python 可以计算超级大的数据
print(2 ** 1000000)

print(type(2**1000000))

# 数字类型可以参与计算
aa = True

print(123 * aa)

aa = False
print(aa * 123)

# 字符串相加就是拼接


one = "大海"
two = "是的"

print(one+two)

print(one*10)

num = 32
num2 = int("18")
print(num*num2)



# 字符串和数字不能直接运算 需要转换
