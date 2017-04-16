#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# ===========================================
#      FileName: fibonacci.py
#          Desc:
#        Author: ruizhong.li
#       Version:
#    CreateTime: 2017-04-16
# ==========================================
"""

def fibonacci(num):
    a = 1
    b = 1
    i = 0

    while i < num:
        print a
        a,b = b,a+b
        i += 1

if __name__ == '__main__':
    num = int(input("Please Input A Num:"))
    fibonacci(num)
