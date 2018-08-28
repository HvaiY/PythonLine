def input_passwd():
    pwd = input("请输入密码：")
    if len(pwd) >= 8:
        return pwd
    ex = Exception("密码长度不够8位")
    raise ex  # 主动抛出实例化的异常


# 处理异常 接收主动抛出的异常
try:
    print(input_passwd())
except Exception as result:
    print(result)
