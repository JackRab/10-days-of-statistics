"""
Objective
In this challenge, we learn about Poisson distributions. 

Task
A random variable, X, follows Poisson distribution with mean of 2.5. 
Find the probability with which the random variable X is equal to 5.
"""
from math import exp, factorial
def poisson(lam=2.5, k=5):
    """
    Return the probability of X=k with possion distribution with mean lam
    """
    return lam**k*exp(-lam)/factorial(k)

print(round(poisson(), 3))