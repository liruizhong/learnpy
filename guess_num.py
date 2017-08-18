#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===========================================
     FileName: guess_num.py
         Desc:
       Author: ruizhong.li
      Version:
   CreateTime: 2017-04-29
==========================================
"""
correct_num = 6
count = 0

while count < 3:
    if count == 0:
        print("This is your %s guess" % (count+1))
        a = int(input("Please input a number:"))
    else:
        print("Please enter again，This is your %s guess" % (count+1))
        a = int(input("Please input a number:"))

    if a < correct_num:
        print("The number you entered is less than the correct number\n")
        print("*******************************************************")
        count += 1
        continue
    elif a == correct_num:
        print("Congratulations on your guess，The correct_num is %s\n" % (correct_num))
        break
    else:
        print("The number you entered is more than the correct number\n")
        print("*******************************************************")
        count += 1
        continue
    count += 1
else:
    print("I'm sorry you didn't get it right 3 times\n")
