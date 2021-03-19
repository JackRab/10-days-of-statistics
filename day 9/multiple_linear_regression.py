"""
Link: 
https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem

Objective
In this challenge, we practice using multiple linear regression. 
"""

import numpy as np 

def find_beta(X, Y):
    """
    Find the coefficient beta give matrix X (independent variables), and Y (dependent variable)
    """
    return np.dot( np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y) )


n, m = [int(s) for s in input().strip().split()]
X_list =[]
Y_list = []
for i in range(m):
    xy = [float(s) for s in input().strip().split()]
    x = [1.0] + xy[:n]
    y = xy[n]
    X_list.append(x)
    Y_list.append(y)

X = np.array(X_list).reshape(m, n+1)
Y = np.array(Y_list).reshape(m, 1)

beta = find_beta(X, Y)

q = int(input())
X_p_list = []
for i in range(q):
    x = [1.0] + [float(s) for s in input().strip().split()]
    X_p_list.append(x)

X_p = np.array(X_p_list).reshape(q, n+1)
Y_p = np.dot(X_p, beta)

for y in Y_p:
    print(round(y[0], 2))