#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 17:48:40 2021

@author: wangchenxi
"""

'''测试debuging功能,开始debug时默认从前向后开始，如果有断点就从头一直执行到断点句之前，执行到调用函数语句时，如果是单步调试会直接将函数当做一句话执行完，如果想进入函数一步步执行，需要点step into，如果在函数内不想一步步执行，直接执行到函数结束，就按step out'''

def test():
    global d
    d=4
def main():
    global a,b,c,e
    a=1
    b=2
    c=3
    test()
    e=5
    
if __name__ == '__main__':
    main()
    print(a,b,c,d,e)