"""
This Question is from https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
Level Easy
"""
import zlib

"""
Question:

You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

"""

"""
SudoCode:

take user input using while loop 
put tuple into list 
sort list using lambda and key in list sort function 

         

"""
database = []
while True:
    string = input()
    if not string:
        break

    info_tuple = string.split(",")
    database.append(tuple([info_tuple[0],int(info_tuple[1]),int(info_tuple[2])]))

import operator
#s = sorted(s, key = operator.itemgetter(1, 2))
sorted_database = sorted(database,key=lambda x:(x[0],x[1],x[2]))
print(sorted_database)
