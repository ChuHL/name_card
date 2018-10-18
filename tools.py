#!/usr/bin/env python 
# -*- coding:utf-8 -*-

cards_list = []

def show_menu():

    """显示菜单"""
    print("*" * 50)
    print("欢迎使用    v 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)

#增加
def add_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")

    #card_dict = {}

    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    QQ_str = input("请输入QQ：")
    Email_str = input("请输入email：")

    card_dict = {"name" : name_str,
                 "phone" : phone_str,
                 "QQ" : QQ_str,
                 "Email" : Email_str}
    cards_list.append(card_dict)
    print(cards_list)
    print("成功添加：%s" % name_str)

#显示
def show_card():

    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    #判断是否有名片记录
    if len(cards_list) == 0:
        print("没有记录，请使用新增功能添加名片")

        #return 可以返回一个函数的执行结果
        #return下方的代码不会执行 没有参数就返回调用代码位置继续执行
        return

    #显示标题
    for name in ["姓名", "电话", "QQ", "邮箱"]:
    #for name in ["姓名","QQ","电话","邮箱"]:
        print(name, end="\t\t\t")

    print("")
    print("=" *50)

    for card_dict in cards_list:
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"],
                                              card_dict["phone"],
                                              card_dict["QQ"],
                                              card_dict["Email"]))


# 查询
def search_card():

    """查询名片"""
    print("-" * 20)
    print("查询名片")

    find_name = input("请输入要查找的姓名：")

    for card_dict in cards_list:

        if card_dict["name"] == find_name:
            print("找到了%s" % find_name)
            print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
            print("=" * 50)
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["QQ"],
                                            card_dict["Email"]))
            #  针对找到的进行修改
            deal_card(card_dict)


            # 找到后退出循环
            break
    else:
        print("没找到%s" % find_name)


# 修改删除
def deal_card(find_dict):

    """处理查找到的名片 修改删除

    :param find_dict: 查找到的名片
    """
    # print(find_dict)
    action_str = input("请选择要执行的操作："
                       "[1]修改  [2]删除  [0]返回  ")
    if action_str == "1":
        print("修改名片")
        # find_dict["name"] = input("姓名：")
        # find_dict["phone"] = input("电话：")
        # find_dict["QQ"] = input("QQ：")
        # find_dict["Email"] = input("邮箱：")
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["QQ"] = input_card_info(find_dict["QQ"], "QQ：")
        find_dict["Email"] = input_card_info(find_dict["Email"], "邮箱：")

        print("修改名片完成")

    elif action_str == "2":
        cards_list.remove(find_dict)
        print("删除名片")


def input_card_info(dict_value, tip_message):
    """输入名片信息

    :param dict_value:字典中原有的值
    :param tip_message:输入提示
    :return:返回修改值，若为空返回原有值
    """
    # 1.提示用户输入
    result_str = input(tip_message)

    # 2.判断是否有输入，有！将内容返回
    if result_str > "0":
        return result_str

    #3.没有！将原来的值返回
    else:
        return dict_value


