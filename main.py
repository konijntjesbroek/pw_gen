from string import ascii_lowercase as l, ascii_uppercase as u, digits as d
from random import choice as rc

pw_length = int(input('How long: ').strip()) - 1
pw_count = int(input('How many: ').strip())

print('\n'.join([rc(l+u)+''.join([rc(l+u+d)
                for _ in range(pw_length)]) 
                for _ in range(pw_count)]))