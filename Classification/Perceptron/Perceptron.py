#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@author yangmu
@version 0.1
@date 2016-03-04
'''

# This file is the implementation of perceptron learning algorithm.
# Here, let's initialize w is a 2 dimention vectors, and b is 0 at the same time.
# What's more, the learning ratio is 1

import os


#test data
training_set = [[(3, 3), 1], [(4, 3), 1], [(1, 1), -1], [(1, 2), -1]]
w = [0, 0]
b = 0

# update parameters using stochastic gradient descent
def updateWB(item):
    global w, b
    w[0] = w[0] + 1 * item[1] * item[0][0]
    w[1] = w[1] + 1 * item[1] * item[0][1]
    b = b + 1 * item[1]
    print w, b

# calculate the functional distance between 'item' an the decision surface
def cal(item):
    global w, b
    res = 0
    for i in range(len(item[0])):
        res += item[0][i] * w[i]
    res += b
    res *= item[1]
    return res

# check if the hyperplane can classify the examples correctly
def check():
    flag = False
    for item in training_set:
        if cal(item) <= 0:
            flag = True
            updateWB(item)
    if not flag:
        print "RESULT: w: " + str(w) + " b: "+ str(b)
        os._exit(0)
    flag = False

if __name__ == '__main__':
    for i in range(1000):
        check()
    print "The training_set is not linear separable."