"""
Spearman's rank correlation coefficient

Link: https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient
"""
def rank(X):
    """
    Return the rank of each element in X
    """
    sorted_X = sorted(X)
    rank = [0]*len(X)
    for i in range(len(X)):
        # since index is zero-based, plus 1 to get the rank
        rank[i] = sorted_X.index(X[i]) + 1

    return rank 

def spearman_corr(X, Y):
    assert len(X) == len(Y)

    sum = 0
    N = len(X)
    rank_x = rank(X)
    rank_y = rank(Y)
    for i in range(N):
        sum += (rank_x[i] - rank_y[i])**2

    return 1 - 6*sum/N/(N**2 - 1)

n = int(input())
X = [float(s) for s in input().split()]
Y = [float(s) for s in input().split()]

print(round(spearman_corr(X, Y), 3))