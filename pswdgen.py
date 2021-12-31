# This program will generate a 8 or 16 characer password
# Written by Gataz in 2021.12.31

# Get the random Library
import random

# Set up the function for user input
def workable():
    
    # Acceptable answer definition
    true_lenght = [16, 8]
    
    # Conditioning...
    if lenght in true_lenght:
        password = "".join(random.sample(all, lenght))
        # This part needs to be improved
        # Do not allow 'special' and 'numbers' to be the password[0]
        print(password)
    
    # If the answer is not valid...
    else:
        print("Can't generate your password")

# Valid password characters
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '012356789'
special = "~! @#$%^&*()_-+={[}]|\:;<,>.?/"

# Group up in one variable
all = lower + upper + numbers + special

# Set up user input
lenght = int(input('Insert characters number here (8 or 16): '))

# Check input and print output
workable()