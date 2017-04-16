#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# ===========================================
#      FileName: fibonacci3.py
#          Desc:
#        Author: ruizhong.li
#       Version:
#    CreateTime: 2017-04-16
# ==========================================
"""

def fibonacci(num):
    numList=[1,1]
    for i in range(num-2):
        numList.append(numList[-2]+numList[-1])
    return numList

if __name__ == '__main__':
    num = int(input("Please Input A Num："))
    print fibonacci(num)
