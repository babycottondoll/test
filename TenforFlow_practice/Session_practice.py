#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 13:59:11 2021

@author: wangchenxi
"""

'''
Session会话控制
'''
import tensorflow.compat.v1 as tf

matrix1=tf.constant([[3,3]])#1行2列的matirx
matrix2=tf.constant([[2],
                     [2]])#2行1列
product=tf.matmul(matrix1,matrix2)#矩阵乘法 类似numpy的np.dot(m1,m2)

#方法1
sess=tf.Session()
result=sess.run(product)#每次run就执行一次product方法
print(result)
sess.close()

#方法2
with tf.Session() as sess:#打开Session命名为sess，运行完后会自动关上sess，最后不用close
    result2=sess.run(product)
    print(result2)
    