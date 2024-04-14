# -*- coding: utf-8 -*-
#
# 字符串工具类

def isNull(str):
    if len(str)==0 or str=='':
        print(str)
        return True;
    print(str)
    return False;


def isNotNull(str):
    if len(str)==0 or str=='':
        return False;
    return True;