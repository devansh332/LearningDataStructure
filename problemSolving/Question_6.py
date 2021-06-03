"""
This Question is from https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
Level Easy
"""

"""
Question:

A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

"""

"""
SudoCode:

declare origin for cartesian place 
for up method add to y axis and for down substract 
similarly add for right and subtract from x when left

calculate distance using sqrt(a**2 + b**2)
         

"""
from math import sqrt
x = y = 0

while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    steps = int(steps)
    if direction.lower() == "right":
        x += steps
    elif direction.lower() == "left":
        x -= steps
    elif direction.lower() == "up":
        y += steps
    elif direction.lower() == "down":
        y -= steps
    else:
        print(" Please select a valid movement option from Up Down Left Right with number of setps")

print(x,y)
print(int(sqrt(x**2+y**2)))