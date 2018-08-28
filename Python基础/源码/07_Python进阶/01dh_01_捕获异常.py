try:
    # 不能确定能正确执行的代码
    num = int(input("请输入一个整数"))
except Exception as msg:
    # 错误处理代码
    print("请输入正确的整数%s" % msg)

print("-" * 50)
