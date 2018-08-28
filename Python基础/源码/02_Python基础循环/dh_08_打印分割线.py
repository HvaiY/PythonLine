def print_line(char, times):
    """打印分割线"""
    print(char * times)


print_line("*", 30)
print("\n")


def print_lines(char, times, lines):
    """打印多行分割线

    :param char: 分割线使用字符
    :param times: 分割线重复的次数
    :param lines: 分割线的行数
    """
    row = 0
    while row <= lines:
        print_line(char, times)
        row += 1


print_lines("-", 17, 6)
