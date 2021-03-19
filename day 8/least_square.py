"""
Link: https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem
"""

def mean(nums):
    """
    Return the mean of nums
    """
    assert len(nums) != 0
    sum = 0
    for n in nums:
        sum += n

    return sum/len(nums)

def least_square(Y, X):
    """
    Return the fitted coefficients of least square (a, b)
    Formula: b = (Sum(X[i] - x_bar)(Y[i] - y_bar)) / (Sum(X[i] - x_bar)**2)
             a = y_bar - b
    """
    # find the mean of X and Y
    mean_x, mean_y = mean(X), mean(Y)

    numerator, denorminator = 0, 0
    for i in range(len(X)):
        numerator += (X[i] - mean_x)*(Y[i] - mean_y)
        denorminator += (X[i] - mean_x)**2

    b = numerator / denorminator
    a = mean_y - b*mean_x
    return a, b

# read 5 lines of input
X, Y = [], []
for i in range(5):
    x, y = [int(s) for s in input().split()]
    X.append(x)
    Y.append(Y)

a, b = least_square(Y, X)
print(round(a+b*80, 3))

""" a very clean solution """
# n = 5
# xy = [map(int, input().split()) for _ in range(n)]
# sx, sy, sx2, sxy = map(sum, zip(*[(x, y, x**2, x * y) for x, y in xy]))
# b = (n * sxy - sx * sy) / (n * sx2 - sx**2)
# a = (sy / n) - b * (sx / n)
# print('{:.3f}'.format(a + b * 80))
