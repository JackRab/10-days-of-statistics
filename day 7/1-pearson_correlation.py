"""
Pearson correlation coefficient
Link: https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem
"""
from math import sqrt
def mean(nums):
    assert len(nums) != 0
    sum = 0
    for n in nums:
        sum += n

    return sum/len(nums)

def std(nums):
    assert len(nums) != 0
    mu = mean(nums)
    var = 0
    for n in nums:
        var += (n - mu)**2

    return sqrt(var/len(nums))

def pearson_corr(X, Y):
    assert len(X) == len(Y)
    mean_x = mean(X)
    mean_y = mean(Y)
    sigma_x = std(X)
    sigma_y = std(Y)
    sum = 0
    for i in range(len(X)):
        sum += (X[i] - mean_x)*(Y[i] -mean_y)

    return sum/sigma_x/sigma_y/len(X)

n = int(input())
X = [float(s) for s in input().split()]
Y = [float(s) for s in input().split()]

print(round(pearson_corr(X, Y), 3))