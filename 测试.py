# -*- coding: utf-8

dct = {'Name': ['Alice','1456'], 'Age':[ 'aa','5aa','345']}
# 取出字典的值
for value1 in dct.values():
   #遍历值列表
    for value2 in value1:
        #判断是否为数字的字符串
        if value2.isdigit():
            value = value1
            key = [k for (k,v) in dct.items() if v == value]
            print("键名:%s" %(str(key)))
            print("对应的值:%s" %(str(value)))
