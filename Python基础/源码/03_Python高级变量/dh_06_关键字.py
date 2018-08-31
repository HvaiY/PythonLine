# 在　Python 中　关键字是没有括号可以直接使用的
# 函数是需要使用括号的　还有参数
import keyword
# 打印所有关键字
print(keyword.kwlist)

print(len(keyword.kwlist))
# 关键字 总共 35个 2018-8-29 其实不多  基本都能在其它语言中找到  意义差不多(面向对象基本一致)
#['False', 'None', 'True', 'and', 'as', 'assert',
#  'async', 'await', 'break', 'class', 'continue', 
# 'def', 'del', 'elif', 'else', 'except', 'finally',
#  'for', 'from', 'global', 'if', 'import', 'in', 
# 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
# 'raise', 'return', 'try', 'while', 'with', 'yield']