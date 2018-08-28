# 使用__name__ 可以本模块执行是__main__ 如果是别人引入 打印的是模块名称


def say():
    print("呵呵")


print(__name__)

if __name__ == "__main__":
    say()
    print("hehe")
