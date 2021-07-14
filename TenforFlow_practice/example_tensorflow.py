#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 10:53:36 2021

@author: wangchenxi
"""

'''
莫烦python课程中tensorflow应用
'''
import tensorflow.compat.v1 as tf
import numpy as np
tf.compat.v1.disable_eager_execution()#可以用于从TensorFlow 1.x到2.x的复杂迁移项目的程序开头
#创造data
x_data=np.random.rand(100).astype(np.float32)
y_data=x_data*0.1+0.3#要预测的结果

#开始创造tensorflow结构
Weights=tf.Variable(tf.random.uniform([1],-1.0,1.0))#随机生成随机一维数列，范围是-1到1之间，作为初始参数变量
biases=tf.Variable(tf.zeros([1]))#初始偏置是0

y=Weights*x_data+biases

loss=tf.reduce_mean(tf.square(y-y_data))#计算预测y与实y_data之间的loss函数
optimizer=tf.train.GradientDescentOptimizer(0.5)#梯度下降优化器,有很多种优化器，这是其中基础的一种，学习效率learning_rate是0.5，一般小于1
train=optimizer.minimize(loss)#用优化器减少loss函数，每一步都要做

init=tf.global_variables_initializer()#初始化结构
#tensorflow结构创建完毕

sess=tf.Session()
sess.run(init)#Session指针指向init结构，激活神经网络初始化结构

for step in range(201):#训练201步
    sess.run(train)#Session指针指向train结构
    if step%20==0:#每20步打印一个结果
        print(step,sess.run(Weights),sess.run(biases))
        
