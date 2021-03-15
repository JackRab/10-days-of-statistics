"""
Objective
In this challenge, we learn about geometric distributions.

Task
The probability that a machine produces a defective product is 1/3. 
What is the probability that the 1st defect occurs the 5th item produced?
"""

def defect(p=1/3, n=5):
    return (1-p)**(n-1)*p 

print(round(defect(), 3))