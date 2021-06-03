"""
This Question is from https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
Level Easy
"""

"""
Question:

A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

"""

"""
SudoCode:

create a validator function use that filter out from the list the password 
print remaing data 
         

"""


def validate_password(password: str) -> bool:
    """
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
    :param password:
    :return:
    """
    if 6 <= len(password) <= 12:
        small_alpha_check = 0
        num_check = 0
        capital_alpha_check = 0
        special_alpha_check = 0
        for i in password:
            if i.islower():
                small_alpha_check += 1
            elif i.isupper():
                capital_alpha_check += 1
            elif i.isdigit():
                num_check += 1
            else:
                special_alpha_check += 1
        if all([small_alpha_check, num_check, capital_alpha_check, special_alpha_check]):
            return True

    return False


pass_list = input().split(',')
print(','.join(list(filter(validate_password, pass_list))))
