#You are given an array that holds the square footage data for houses on a particular street.
#A new house has just been constructed on that street.
#Modify your program to take the new house value as input, add it to the array, and output the array sorted in ascending order.
#Use the print statement to output the array object.


import numpy as np

data = np.array([1000, 2500, 1400, 1800, 900, 4200, 2200, 1900, 3500])

new_house = int(input())

data = np.append(data, new_house)

data = np.sort(data)

print(data)