"""
Objective
In this challenge, we go further with Poisson distributions.

Task
The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:

The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. 
The daily cost of operating A is C_A = 160+40X^2.
The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. 
The daily cost of operating B is C_B = 128+40Y^2.
Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that 
they operate like new at the start of each day. 
Find and print the expected daily cost for each machine.
"""

import numpy as np

def daily_cost(lam=0.88, intercept=160):
    """
    Return the expected daily cost for machine with lam and intercept
    """
    # for a poisson distribution, E(X) = lam, Var(X) = lam, 
    # since E(X-E(X))^2 = E(X^2) - (EX)^2, 
    # then E(X^2) = Var(X) + (EX)^2
    return intercept + 40*(lam + lam**2)

# print the expected daily cost for machine A
print(np.round(daily_cost(), 3))
# print the expected daily cost for machine B
print(np.round(daily_cost(lam=1.55, intercept=128), 3))