"""Module to run Conway's Game of Life taking user inputs.

This module takes height and width of game, and random seed from the user
as command line argument and runs the game for 100 iterations

AUTHOR: sp936
"""

from random import random
import time
import a5 

height = int(input("[@] Enter height : "))
width = int(input("[@] Enter width : "))

random_seed = int(input("[@] Enter a random seed : "))

life = a5.Life(width, height)
life.randomize(random_seed)

for i in range(100):
    life.print()
    life.next()
    time.sleep(0.5)
