"""
This Question is from https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
Level Easy
"""

"""
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
"""

"""
SudoCode:

define function factorial 
    add base case for 0 and 1 
    return product to n and factorial(n-1)
    
assign return number to fact identifier
print identifier

"""


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(8))
