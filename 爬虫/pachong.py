#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 18:56:37 2021

@author: wangchenxi
"""

'''
爬虫爬取网站数据
'''

#mport xpath
import requests
import xlwt


#定义请求的url
url='http://www.baidu.com/'#https是私密地址
#发起get请求
res=requests.get(url)
#获取响应结果
print(res)#<Response [200]>面相对象封装好的res
print(res.content)#b'......'二进制的文本流
print(res.content.decode('utf-8'))#把二进制的文本流按照utf8字符集转换成普通文本字符串
print(res.text)#获取响应内容，与content。decode一样
print(res.headers)#响应头信息
print(res.status_code)#请求状态码 200
