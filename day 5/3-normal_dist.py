"""
Objective
In this challenge, we learn about normal distributions.

Task
In a certain plant, the time taken to assemble a car is a random variable, X, 
having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. 
What is the probability that a car can be assembled at this plant in:

1. Less than 19.5 hours?
2. Between 20 and 22 hours?
"""

from math import erf, sqrt

def cdf_norm(mu=20, sigma=2, lower=-float('inf'), upper=19.5):
    """
    Return the cumulative probability of normal distribution
    """
    return 0.5*(1+erf((upper - mu)/sigma/sqrt(2))) - 0.5*(1+erf((lower - mu)/sigma/sqrt(2)))

# print the probability less than 19.5 hours
print(round(cdf_norm(), 3))
# print the probability between 20 and 22 hours
print(round(cdf_norm(lower=20, upper=22), 3))