# 搜索一个 字典列表  使用for else
students = [
    {"name": "阿土"},
    {"name": "小美"}
]

find_name = "张三"  # 妙用 张三 小美 试试效果

for student in students:
    print(student)
    if student["name"] == find_name:
        print("找到%s了" % find_name)
        break
else:
    print("抱歉没有找到%s" % find_name)
