"""
This Question is from https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
Level Easy
"""

"""
Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
"""

"""
SudoCode:

use dictionary comprehesion for construct a dict of squares 
print the created dictionry

"""
n = 4
square_dict = {i: i ** 2 for i in range(1, n + 1)}
print(square_dict)
