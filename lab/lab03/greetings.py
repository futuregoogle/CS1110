# greetings.py
# sp936
# June 23rd
# Skeleton by Tobias Kappe, June 2021
# Based on work by Prof. L. Lee, January 2020

"""Library of functions producing greetings"""

import random

input_name = input('Please enter your name: ')
reps = random.randint(1,6)
output = "hi " * reps + input_name + "!"

print(output)
