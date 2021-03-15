"""
In this challenge, we're reinforcing what we've learned today. 

Task
A bag contains 3 red marbles and 4 blue marbles. Then, 2 marbles are drawn from the bag, at random, without replacement. 
If the first marble drawn is red, what is the probability that the second marble is blue?
"""

import numpy as np

def second_blue(N=10000):
    num_1red = 0
    num_1red_2blue = 0
    for i in range(N):
        # suppose 0-2 are red, 3-6 are blue
        # draw the first marble
        marble1 = np.random.randint(0, 7)

        # draw the second marble
        marble2 = np.random.randint(0, 7)
        # if the same, then redraw
        while marble2 == marble1:
            marble2 = np.random.randint(0, 7)

        if marble1<= 2:
            num_1red += 1
            if marble2 in range(3, 7):
                num_1red_2blue += 1

    # conditional probability
    return num_1red_2blue / num_1red