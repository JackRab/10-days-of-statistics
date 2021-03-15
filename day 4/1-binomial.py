"""
Objective
In this challenge, we learn about binomial distributions.

Task
The ratio of boys to girls for babies born in Russia is 1.09:1. 
If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. 
Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).

"""
from math import factorial
def binomial(p=1.09/(1.09+1)):
    """
    Return the probability of at least 3 boys for a family with 6 children
    """
    
    prob = 0.0
    for i in range(3, 7):
        # prob of i boys (6 choose i)
        
        prob += factorial(6)/factorial(i)/factorial(6-i)*p**i*(1-p)**(6-i)

    return prob

print(round(binomial(), 3))