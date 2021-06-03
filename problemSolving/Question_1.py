"""
This Question is from https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
Level Easy
"""

"""
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

"""
SudoCode:

loop through range of 2000 to 3201
    check for divisibility by 7 and not by 5 
        add number to list

print the list using join funtion

"""

numbers = []

for number in range(2000,3201):
    if number % 7 ==0 and number%5!=0:
        numbers.append(number)

print(",".join(map(str,numbers)))

