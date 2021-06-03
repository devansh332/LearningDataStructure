"""
This Question is from https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
Level Easy
"""

"""
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,-1.

"""

"""
SudoCode:
declare table 
for loop for i
    declare column
    for loop for j
        append i*j into column list
    append column list to table 

print table 
         

"""

matrix = []
X,Y = 3,5

for i in range(X):
    column = []
    for j in range(Y):
        column.append(i*j)
    matrix.append(column)

print(matrix)