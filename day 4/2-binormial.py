"""
Objective
In this challenge, we go further with binomial distributions.

Task
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because 
they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

1. No more than 2 rejects?
2. At least 2 rejects?
"""

from math import factorial

def pistons(p=0.12, n=10):
    # no more than 2 rejects
    prob_no_more_than_2, prob_at_least_2 = 0, 1
    for i in range(0, 3):
        prob_i = factorial(10)/factorial(i)/factorial(10-i)*p**i*(1-p)**(10-i)

        prob_no_more_than_2 += prob_i

        if i != 2:
            prob_at_least_2 -= prob_i

    return prob_no_more_than_2, prob_at_least_2

p1, p2 = pistons()
print(round(p1, 3))
print(round(p2, 3))