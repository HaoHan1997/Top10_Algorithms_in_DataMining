#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@version 0.1
@date 2016-03-06
'''

# This file is the implementation of linear regression.
# The experimental data is testSet in the same directory.


from numpy import *

def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of features
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

def standRegres(xArr,yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws

if __name__ == '__main__':
    fileName = './testSet'
    xArry, yArry = loadDataSet(fileName)
    ws = standRegres(xArry, yArry)

    print 'The weight value is:'
    print ws
