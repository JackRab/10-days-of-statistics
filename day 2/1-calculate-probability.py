"""
In this challenge, we practice calculating probability.

Task
In a single toss of 2 fair (evenly-weighted) six-sided dice, 
find the probability that their sum will be at most 9.
"""

import numpy as np

def calculate_prob(N=10000):
    """
    Use simulation to calculate probability of the sum of 2 faid six-sided dice 
    if at most 9
    """

    times_less_or_equal_to_9 = 0
    for i in range(N):  
        # toss dice once
        d1 = np.random.randint(1, 7)
        # toss dice again
        d2 = np.random.randint(1, 7)

        if d1 + d2 <= 9:
            times_less_or_equal_to_9 += 1


    return times_less_or_equal_to_9 / N