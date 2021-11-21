""" Author of the code: Ashdika Nusrat Siddiqee
Module: PDE1130
MISIS number: M00847293

My first mini project about how users can get their passwords automatically generated using the given characters. Since mass population use social media, you can input the required number and length of the passwords to use them for various platforms on the internet or needed to change into different passwords to keep their data protected."""

import random

print("Welcome to your Password Generator")

# The characters that will be used to generate passwords
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

# The user will input the number of passwords he/she requires
number = input("Number of passwords to generate: ")
number = int(number)

length = input("Input the length of your password: ")
length = int(length)

print('\n Here are your passwords: ')

# This will randomly generate the password according to the user's inputs
for i in range(number):
    passwords = ''
    for j in range(length):
        passwords += random.choice(chars)
    print(passwords)
