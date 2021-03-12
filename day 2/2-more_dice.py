"""
In this challenge, we practice calculating probability.

Task
In a single toss of 2 fair (evenly-weighted) six-sided dice, 
find the probability that the values rolled by each die will be different and the two dice have a sum of 6.


"""

import numpy as np 

def calculate_prob(N=10000):
    num = 0
    for i in range(N):
        # roll dice once
        d1 = np.random.randint(1, 7)
        # roll dice again
        d2 = np.random.randint(1, 7)    
        if d1 != d2 and d1+d2 == 6:
            num += 1

    return num / N