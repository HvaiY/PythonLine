def print_menu():
    """显示菜单"""
    print("*" * 50)
    print("")
    print('欢迎使用【卡片管理系统】V1.0')
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("")
    print("*" * 50)


card_list = []


def new_card():
    """新增名片"""
    print("新增名片")
    name_str = input("请输入名字")
    phone_str = input("请输入电话号码")
    email_str = input("请输入邮箱")
    qq_str = input("请输入QQ号码")
    # 添加到列表中
    card_dic = {"name": name_str,
                "phone": phone_str,
                "email": email_str,
                "qq": qq_str}
    card_list.append(card_dic)
    print("添加成功！")


def show_all():
    """显示所有名片"""
    print("功能：显示全部")
    for str in ["姓名", "电话", "邮箱", "QQ"]:
        print(str, end="\t\t")
    print("")
    print("=" * 50)
    for card_dic in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dic["name"], card_dic["phone"], card_dic["email"], card_dic["qq"]))


def search_card():
    """搜索名片"""
    print("搜索名片")
