#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：puke 
@File ：util.py
@Author ：抱着欣欣看月亮
@Date ：2021/10/21 20:55 
'''
import requests

def login(username,password):
    res = requests.post(url="http://172.17.173.97:8080/api/user/login",data={"student_id":username,"password":password}).json()
    status = res["status"]
    if status == 200:
        return True,res["data"]
    else:
        return False,res["data"]
    
# login("041901413","hts2953936")
    