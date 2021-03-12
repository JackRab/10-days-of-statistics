"""
In this challenge, we practice calculating the probability of a compound event. 

Task
There are 3 urns labeled X, Y, and Z.

Urn 1 contains 4 red balls and 3 black balls.
Urn 2 contains 5 red balls and 4 black balls.
Urn 3 contains 4 red balls and 4 black balls.

One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?
"""


import numpy as np
    
def redblack(N=10000):
    num = 0

    for i in range(N):
        # draw b1 from 1 to 7, suppose 1 to 4 are red
        b1 = np.random.randint(1, 8)
        # draw b2 from 1 to 9, suppose 1 to 5 are red
        b2 = np.random.randint(1, 10)
        # draw b3 from 1 to 8, suppose 1 to 4 are red
        b3 = np.random.randint(1, 9)
    
        red = 0
        if b1 <= 4:
            red += 1
        if b2 <= 5:
            red += 1
        if b3 <= 4:
            red += 1
    
        if red == 2:
            num += 1
    return num / N
