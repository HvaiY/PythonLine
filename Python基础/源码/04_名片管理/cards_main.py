#! /usr/bin/python3

import cards_tools

# 希望能够在linux终端中执行 这个py主程序 需要加上shebang #! 和解释器路径 也就是python路径

while True:
    #  显示功能菜单
    cards_tools.print_menu()
    action_str = input("请选中希望执行的动作:")
    print("您选择的动作是：%s" % action_str)
    if action_str in ["1", "2", "3"]:

        if action_str == "1":

            cards_tools.new_card()

        elif action_str == "2":

            cards_tools.show_all()

        elif action_str == "3":

            cards_tools.search_card()

    elif action_str == "0":
        print("欢迎再次使用系统，再见")
        break  # 退出循环
        pass  # 可以跳过通过当前的 暂时不写代码,但保存代码完整
    else:
        print("您输入的有误，还请重新操作")
