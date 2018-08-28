# 列表是有序的对象集合，　然后，字典是无序的对象集合　dictionary
# 字典　键值对集合　dictionary
# 键　key　必须是唯一的
student_dic = {"name": "老张",
               "age": 18,
               "gender": True,
               "height": 1.75,
               "weight": 75}

# 增删改查

student_dic.pop("gender")
student_dic["age"] = 19
print(student_dic["name"])

print(student_dic)  # 无序显示

# 其它操作
print("*" * 150)
# 统计数量
print(len(student_dic))
# 合并字典
ss = {"address": "上海"}
student_dic.update(ss)  # 如果出现了相同的key　那么使用update合并的话　后面的key值可以替换前面的值

print(student_dic)
