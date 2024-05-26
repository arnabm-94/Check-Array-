
'''
Write a program to check if an array contains a number in python

'''

import numpy as np 

# Creating the array
myArray = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25])

# Creating a function with two arguments: array and number 
def findNumber(array, number):
    found = False  # Flag to track if the number is found
    for i in range(len(array)):
        if array[i] == number:
            print(i)  # Print the index of this element i
            found = True
            break  # Exit the loop once the number is found
    if not found:
        print("Number not found in the array.")

findNumber(myArray, 13)
