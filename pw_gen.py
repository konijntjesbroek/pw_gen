#!/usr/bin/python3

from sys import argv
from string import ascii_lowercase as l, ascii_uppercase as u, digits as d
from random import choice as rc

USAGE = '''pw_gen (<lenghth>) (<count>)
    Prints a number of randomly generated strings beginning with a letter and 
    consisting of lowercase, uppercase, and numeric characters. 
    
    pw_gen
        1 password 8 characters long

    pw_gen x
        1 pasword x characters long
    
    pw_gen x y 
        y passwords x characters long
'''

if len(argv) == 1:
    pw_length = 8
    pw_count = 1
elif len(argv) == 2 and argv[1].isnumeric():
    pw_length = int(argv[1]) - 1
    pw_count = 1
elif len(argv) == 3 and argv[1].isnumeric() and argv[2].isnumeric():
    pw_length = int(argv[1]) - 1 
    pw_count = int(argv[2])
else:
    print(USAGE)
    exit(1)

# pw_length = int(input('How long: ').strip()) - 1
# pw_count = int(input('How many: ').strip())

print('\n'.join([rc(l+u)+''.join([rc(l+u+d)
                for _ in range(pw_length)]) 
                for _ in range(pw_count)]))
