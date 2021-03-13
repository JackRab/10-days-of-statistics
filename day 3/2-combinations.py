"""
In this challenge, we're getting started with combinations and permutations.

Task
You draw 2 cards from a standard 52-card deck without replacing them. 
What is the probability that both cards are of the same suit?
"""

import numpy as np 

def combination(N=10000):
    num_same_suit = 0
    for i in range(N):
        # suppose we place suit clubs as 0-12, diamonds 13-25, hearts 26-38, spades 39-51
        # first we draw a card from 0-51
        card1 = np.random.randint(0, 52)

        # then we draw another card from 0-51, but must not be same as card1
        card2 = np.random.randint(0, 52)

        # if they are the same, we draw again (Caution: there is a little risk of a infinite loop here)
        while card1 == card2:
            card2 = np.random.randint(0, 52)

        # then we check if the two cards are from the same suit
        if card1 <= 12:
            if card2 <= 12:
                num_same_suit += 1
        elif card1 <= 25:
            if card2>=13 and card2 <= 25:
                num_same_suit += 1
        elif card1 <= 38:
            if card2>=26 and card2 <= 38:
                num_same_suit +=1
        else:
            if card2 >= 39:
                num_same_suit +=1

    return num_same_suit / N

combination()