# last_task.py
# Adapted by Tobias Kappe based on work by Prof Lillian Lee (LJL2)
# June 2021

"""Gives satisfying response when students correctly implement module
greetings"""

import greetings

print()  # print blank line to make output easier to see

if greetings.output is not None and greetings.output.startswith("hi "):
    print("Congratulations on completing your first program for CS1110!!")
else:
    print("It seems that you haven't successfully completed the lab yet.")
