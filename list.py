#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===========================================
     FileName: list.py
         Desc:
       Author: ruizhong.li
      Version:
   CreateTime: 2017-05-01
==========================================
"""
movices = ["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,["Graham Chapman",["Michael Palin","John Class","Terry Gilliam"]]]


def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)



if __name__ == '__main__':
    print_lol(movices)
