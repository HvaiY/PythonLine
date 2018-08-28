try:
    num = int(input("请输入一个整数"))
    result = 8 / num
    print("%.2f" % result)
    # ValueError ZeroDivisionError
except ValueError:
    print("请输入一个整数")
except Exception as result:  # 捕获未知错误
    print("未知错误：%s" % result)
else:
    print("没有错误，我就执行了")
finally:
    print("我最终还是会执行的，不管异常有没有")
print("-" * 50)
