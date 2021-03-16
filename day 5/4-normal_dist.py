"""
Objective
In this challenge, we go further with normal distributions. 

Task
The final grades for a Physics exam taken by a large group of students have a mean of mu=70 and 
a standard deviation of sigma=10. If we can approximate the distribution of these grades by a normal distribution, 
what percentage of the students:

1. Scored higher than 80 (i.e., have a grade > 80)?
2. Passed the test (i.e., have a grade >= 60)?
3. Failed the test (i.e., have a < 60)?
Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.
"""

from math import erf, sqrt

def cdf_norm(mu=70, sigma=10, lower=-float('inf'), upper=80):
    """
    Return the cumulative probability of normal distribution
    """
    return 0.5*(1+erf((upper - mu)/sigma/sqrt(2))) - 0.5*(1+erf((lower - mu)/sigma/sqrt(2)))


# print the probability of grade > 80
print(round(100*(1-cdf_norm()), 2))
# print the probability of grade >= 60
print(round(100*(1-cdf_norm(upper=60)), 2))
# print the probability of grade < 60
print(round(100*(cdf_norm(upper=60)), 2))