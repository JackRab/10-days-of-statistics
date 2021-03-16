"""
Objective
In this challenge, we practice solving problems based on the Central Limit Theorem. 

Task
A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes 
must be transported via the elevator. The box weight of this type of cargo follows a distribution with 
a mean of mu = 205 pounds and a standard deviation of sigma=15 pounds. Based on this information, what is 
the probability that all 49 boxes can be safely loaded into the freight elevator and transported?

"""

from math import erf, sqrt 

def cdf_norm(mu=205, sigma=15, lower=-float('inf'), upper=9800):
    """
    Return the cumulative probability of a normal distribution within a range (lower, upper)
    """
    return 0.5*(1+erf((upper-mu)/sigma/sqrt(2))) - 0.5*(1+erf((lower-mu)/sigma/sqrt(2)))


# by central limit theorem, Sum ~ N(n*mu, sqrt(n)*sigma)
prob = cdf_norm(49*205, sqrt(49)*15)
print(round(prob, 4))


"""
Task
The number of tickets purchased by each student for the University X vs. 
University Y football game follows a distribution that has a mean of mu=2.4 and a standard deviation of sigma=2.0.

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. 
If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?
"""
# by central limit theorem, Sum ~ N(n*mu, sqrt(n)*sigma)
prob = cdf_norm(100*2.4, sqrt(100)*2.0, upper=250)
print(round(prob, 4))


"""
Task
You have a sample of 100 values from a population with mean mu=500 and with standard deviation sigma=80. 
Compute the interval that covers the middle 95% of the distribution of the sample mean; 
in other words, compute A and B such that P(A < x < B) = 0.95. Use the value of z=1.96. Note that z is the z-score.
"""
# the sample mean follows N(mu, sigma/sqrt(n)) by central limit theorem
mu, sigma, n = 500, 80, 100
# sqrt(n)*(A - mu)/sigma = -1.96
A = -1.96*sigma/sqrt(n) + mu 
# sqrt(n)*(B - mu)/sigma = 1.96
B = 1.96*sigma/sqrt(n) + mu 
print(round(A, 2))
print(round(B, 2))