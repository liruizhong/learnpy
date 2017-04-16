#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# ===========================================
#      FileName: fibonacci2.py
#          Desc:
#        Author: ruizhong.li
#       Version:
#    CreateTime: 2017-04-16
# ==========================================
"""

def fibonacci(num):
    if num == 1:
        res = 1
    elif num == 2:
        res = 1
    else:
        res = fibonacci(num-1) + fibonacci(num-2)
    return res

if __name__ == '__main__':
    num = int(input("Please Input A Num:"))
    i = 1
    while i < num:
        print fibonacci(i)
        i += 1
