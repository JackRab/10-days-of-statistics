"""
In this challenge, we get started with conditional probability. 

Task
Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys?
"""

import numpy as np 

def cond_prob(N=10000):
    # choose a random int from [0, 1], if it's 1, it's a boy
    num_at_least_one_boy = 0
    num_two_boys =0
    for i in range(N):
        # draw a number for the first child
        A = np.random.randint(0, 2)

        # draw a number for the second child
        B = np.random.randint(0, 2)

        if A + B >= 1: # at lease one boy
            num_at_least_one_boy += 1

        if A + B == 2: # two boys
            num_two_boys += 1

    # conditional probability
    return num_two_boys/num_at_least_one_boy



