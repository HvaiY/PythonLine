import dh_message

# 愉快的调用 注意安装的包和项目中的包名不要一样哦
dh_message.send_message.send("大海啊")
str_info = dh_message.receive_message.receive("1000")
print(str_info)

print(dh_message.__file__)
# 在04中的操作使用了移除包 所以这里报错
