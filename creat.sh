#!/bin/bash
if [ -z $1 ];then
    echo "used: $0 file"
else
    DATE=`date +%F`
    printf "#!/usr/bin/env python
# -*- coding: utf-8 -*-

\"\"\"
===========================================
     FileName: $1
         Desc: $2
       Author: ruizhong.li
      Version:
   CreateTime: ${DATE}
==========================================
\"\"\"
" > $1

fi
