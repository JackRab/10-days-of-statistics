"""
In this challenge, we practice calculating a weighted mean. 

Given an array, X, of N integers and an array, W , representing the respective weights of 's elements, calculate and print the weighted mean of X's elements. 
Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).
"""
# read the first line as N
N = int(input())

# read the second line and convert it to an array
X = [int(s) for s in input().split()]

# read the third line and convert it to an array
W = [int(s) for s in input().split()]

# calculate the weighted num for each num in X
XW = [X[i]*W[i] for i in range(N)]

# calcuate and print the weighted mean, round to 1 decimal place
weighted_mean = round(float(sum(XW)/sum(W)), 1)
print(weighted_mean)