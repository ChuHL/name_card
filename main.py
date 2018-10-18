#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import tools

while True:

    # 显示内容
    tools.show_menu()
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是：%s" % action_str)

    #1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:

        #新增
        if action_str == "1":

            tools.add_card()
        #显示
        elif action_str == "2":

            tools.show_card()
        #查询
        elif action_str == "3":

            tools.search_card()

    #0 退出系统
    elif action_str == "0":
        print("欢迎再次使用")
        break
        #pass

    #其他内容输入错误，需要重新输入
    else:
        print("输入错误，请重新输入")