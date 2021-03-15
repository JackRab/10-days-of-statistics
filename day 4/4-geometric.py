"""
Objective
In this challenge, we go further with geometric distributions.

Task
The probability that a machine produces a defective product is 1/3. 
What is the probability that the 1st defect is found during the first 5 inspections?
"""

def defect(p=1/3, n=1):
    """
    return the probability of 1st defect is found during the nth inspection
    """
    return (1-p)**(n-1)*p 

# the 1st defect coule be found in 1, 2, 3, 4, 5th inspection
prob = 0
for i in range(1, 6):
    prob += defect(p=1/3, n=i)

print(round(prob, 3))
