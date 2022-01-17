
#importing library
import random
import numpy as test


#defining variables
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


#introduction
print('Welcome to the password generator!')

#Asking how many letters the person would like to have in their password.
r_letters = int(input('How many letters would you like to be included in this password?\n'))

#Asking how many numbers would the person like to have in their password.
r_numbers = int(input('How many numbers would you like to be included in this password?\n'))

#Asking how many other symbols would they like to have in their password.
r_symbols = int(input('How many symbols would you like to be included in this password?\n'))

password = list()

#for loops to select each character in the range of characters selected by the user
for r_letters in range(1, r_letters):
    password += random.choice(letters)

for r_numbers in range(1, r_numbers):
    password += random.choice(numbers)

for r_symbols in range(1, r_symbols):
    password += random.choice(symbols)

#shuffling the password and joining it as a string to be printed
random.shuffle(password)
password = ''.join(password)

#printing the final result
print(f'Your new password is: {password}')