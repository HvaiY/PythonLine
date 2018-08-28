try:
    num = int(input("请输入一个整数"))
    result = 8 / num
    print(result)
    # ValueError ZeroDivisionError
except ValueError:
    print("请输入一个整数")
except ZeroDivisionError:
    print("除数不为0")

print("-" * 50)

# 捕获未知错误
try:
    nums = int(input("请输入一个整数"))
    results = 8 / nums
    print(results)
    # ValueError ZeroDivisionError
except ValueError:
    print("请输入一个整数")
except Exception as result:  # 捕获未知错误
    print("未知错误：%s" % result)
