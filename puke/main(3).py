#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：puke 
@File ：main.py
@Author ：抱着欣欣看月亮
@Date ：2021/10/21 21:52 
'''
import login
import main_page
import people_to_people,people_to_computer


if __name__ == '__main__':
    status = 0 #0:login 1:main_page 2:人人对战
    name = None
    token = None
    while status!=-1:
        if status == 0:
            a = login.Login()
            b = a.run()
            if b["status"] == -1:
                status = -1
            elif b["status"] == 1:
                status = 1
                name = b["name"]
                token = b["token"]
                # print(name,token)
            del a
        if status == 1:
            a = main_page.Main_page(name=name,token=token)
            b = a.run()
            if b["status"] == 2:
                status = 2
            elif b["status"] == 3:
                status = 3
            elif b["status"] == 3:
                status = 4
            elif b["status"] == 0:
                status = 0
                name = None
                token = None
                # print(name,token)
            del a
        if status == 2:
            a = people_to_people.People_to_people()
            b = a.run()
            if b["status"] == 1:
                status = 1
            del a
        if status == 3:
            a = people_to_computer.People_to_computer()
            b = a.run()
            if b["status"] == 1:
                status = 1
            del a
