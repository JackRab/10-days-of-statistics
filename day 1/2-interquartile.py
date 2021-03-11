"""
In this challenge, we practice calculating the interquartile range.

Task
The interquartile range of an array is the difference between its first () and third () quartiles (i.e., ).

Given an array, X, of N integers and an array, F, representing the respective frequencies of X's elements, construct a data set, S, 
where each x_i occurs at frequency f_i. Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).
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

def quartiles(X):
    """
    Return the three quartiles of X 
    """
    # sort the elements of X ascending first
    X_sorted = sorted(X)

    middle = len(X) // 2
    if len(X)%2 == 0: # even number of elements
        X_lower = X_sorted[:middle]
        X_upper = X_sorted[middle:]
    else:
        X_lower = X_sorted[:middle]
        X_upper = X_sorted[middle+1:]

    Q_1 = median(X_lower)
    Q_2 = median(X)
    Q_3 = median(X_upper)

    return Q_1, Q_2, Q_3

# read the first line to get N
N = int(input())

# read the second line to get X
X = [int(s) for s in input().split()]

# read the third line to get F
F = [int(s) for s in input().split()]

# construct S using X and F
S = []
[S.extend([X[i]]*F[i]) for i in range(N)]

# calculate Q_1 and Q_3
Q_1, _, Q_3 = quartiles(S)

print(round(Q_3 - Q_1, 1))
