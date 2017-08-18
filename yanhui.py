#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===========================================
     FileName: yanhui.py
         Desc:
       Author: ruizhong.li
      Version:
   CreateTime: 2017-04-29
==========================================
"""

def row(x):
    return ' '.join(map(str, reduce(lambda x,y: map(sum,zip([0]+x,x+[0])),range(x),[1])))

def pascal(x):
    return '\n'.join(row(i).center(len(row(x-1))) for i in range(x))

print pascal(10)
