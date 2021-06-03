"""
This Question is from https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
Level Easy
"""

"""
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
"""

"""
SudoCode:

split input using split method 
convert data tupe to sequence type 
print both of the result 

"""
n = input().split()
print(n)
print(tuple(n))
