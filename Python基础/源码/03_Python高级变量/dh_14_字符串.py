# 字符串定义　“　‘　两种引号都可以
str1 = "Hello Python"
str2 = '我的外号是"大海"'  # 单引号内部有双引号　相当于转义了　\"

print(str2)
# 字符串还可以遍历
for s in str2:
    print(s)

# 可以单个获取 索引都是0开始的
print(str1[2])