#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:54:50 2021

@author: wangchenxi
"""
'''
测试多线程
'''
import threading
import time

class Mythread(threading.Thread):
    def login(self):
        print('登录')
    def run(self):#此处函数是run在调用start方法后可以自动运行，如果不是run的话需要再在start之后调用这个函数
        for i in range(3):
            time.sleep(1)
            msg='This is %d'%i
            print(msg)
            self.login()
    
        
if __name__ == '__main__':
    t=Mythread()#实例化
    t.start()
    print('主程序继续运行')
    