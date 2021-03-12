"""
In this challenge, we practice calculating standard deviation.
"""

from math import sqrt

def mean(X):
    """
    Return the mean of X
    """
    if not X:
        return None

    sum = 0
    for x in X:
        sum += x 
    return sum/len(X)

def std(X):
    """
    Return the std of X
    """
    if not X:
        return None

    mean_X = mean(X)

    sum_squared_error = 0
    for x in X:
        sum_squared_error += (x - mean_X)**2

    return sqrt(sum_squared_error/len(X))

# read the first line to get N
N = int(input())

# read the second line to get X
X = [int(s) for s in input().split()]

print(round(std(X), 1))