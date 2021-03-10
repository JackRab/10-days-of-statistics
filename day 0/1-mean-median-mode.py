"""
In this challenge, we practice calculating the mean, median, and mode.

Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. 
If your array contains more than one modal value, choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, 
rounded to a scale of 1 decimal place (i.e., 12.3, 7.0 format).

Input Format

The first line contains an integer, N , the number of elements in the array.
The second line contains N space-separated integers that describe the array's elements.

Output Format

Print 3 lines of output in the following order:

1. Print the mean on the first line to a scale of 1 decimal place (i.e., 12.3).
2. Print the median on a new line, to a scale of 1 decimal place (i.e., 12.3).
3. Print the mode on a new line. If more than one such value exists, print the numerically smallest one.

"""

# read the first line as N
N = int(input())

# read the second line and convert it to an array
X_str = input()
X = [int(s) for s in X_str.split()]

def three_stats(N, X):
    """
    Return the mean, median, and mode of X
    """
    # sort X into ascending first (could have writen a sort function, but not the focus here)
    X_sorted = sorted(X)

    # calculate mean by summarizing all numbers
    sum = 0
    # use a dict to store number of appearance for each num
    X_dict = {}
    # store max number of appearance
    max_num_appearance = 0
    mode = X_sorted[0]
    for x in X_sorted:
        sum += x

        X_dict[x] = X_dict.get(x, 0) + 1

        # update mode and max_num_appearance
        if X_dict[x] > max_num_appearance:
            mode = x 
            max_num_appearance = X_dict[x]
        if X_dict[x] == max_num_appearance:
            if x < mode:
                mode = x 


    # calculate median
    if N % 2 == 0: # even
        median = (X_sorted[N//2 -1] + X_sorted[N//2])/2
    else:     # odd
        median = X_sorted[N//2]

    return round(float(sum/N), 1), round(float(median), 1), mode

# calculate three stats and print them out
mean, median, mode = three_stats(N, X)  
print(mean)
print(median)
print(mode)