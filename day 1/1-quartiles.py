"""
In this challenge, we practice calculating quartiles. 
Task
Given an array, X, of N integers, calculate the respective first quartile (Q_1), second quartile (Q_2), 
and third quartile (Q_3). It is guaranteed that Q_1, Q_2, and Q_3 are integers.
"""

# def a function to find median in an array
def median(X):
    """
    Return the median of X
    """
    # sort the elements of X ascending first
    X_sorted = sorted(X)

    middle = len(X) // 2
    if len(X) % 2 == 0: # even number of elements
        return (X_sorted[middle] + X_sorted[middle-1]) / 2
    else:               # odd number of elements
        return float(X_sorted[middle])

# read the first line to get N
N = int(input())

# read the second line to get X
X = [int(s) for s in input().split()]

# fint the median, and convert it to an int
Q_2 = int(median(X))

# sort X and split X into lower half and upper half
X.sort()

middle = N // 2
if N%2 == 0: # even number of elements
    X_lower = X[:middle]
    X_upper = X[middle:]
else:
    X_lower = X[:middle]
    X_upper = X[middle+1:]

Q_1 = int(median(X_lower))
Q_3 = int(median(X_upper))

print(Q_1)
print(Q_2)
print(Q_3)