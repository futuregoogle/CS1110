"""
A script for Assignment 1

This script skeleton uses comments and print statements to help indicate what
you need to do. Read the Assignment 1 document before writing anything in this
script. Do not change or remove any given print statements.  Note that the
print output values are not the correct answers: your job is to change the code
so that the printed values are correct. We provided some variables/values and
the print statements as examples of how to format printing of numeric values.

Author: sp936
Date: 23rd June 2021
"""

print('\n --- Exercise 1 --- ')

# Suppose you are taking a course that assigns grades on a scale of 1 to 100.
# The course has several assignments and a final exam, each of which is
# weighted differently. The grades and weights for the assignments so far are:
# - Assignment 1: grade 87, weight 14%
# - Assignment 2: grade 65, weight 17%
# - Assignment 3: grade 75, weight 19%
# The exam counts for 50% of your grade. Which grade do you need to get on
# this exam to have a final grade of at least 80?

assignment_1 = 87.0
assignment_2 = 65.0
assignment_3 = 75.0
assignment_4 = 85.04
weight_1 = 14.0
weight_2 = 17.0
weight_3 = 19.0
weight_4 = 50.0

min_exam_grade = 85.04

print(f'The minimal exam grade I need is {min_exam_grade:.2f}')


print('\n --- Exercise 2 --- ')

# You are running a triathlon, with the following times:
# - First, you swim for a quarter mile at 1.8 miles per hour;
# - Then, you bike five miles at 12 miles per hour;
# - Finally, you run 1.2 miles at 6.5 miles per hour
# If the starting signal is at 10:45am, at what time do you finish?
# Express your answer in hours and minutes, using ints.
#
# HINT: You can use the % operator to find the remainder of a division. For
# Example, the 7 % 3 returns 1, and 12 % 7 returns 5.


swim_distance = 0.25
swim_speed = 1.8

bike_distance = 5.0
bike_speed = 12.0

run_distance = 1.2
run_speed = 6.5

start_hour = 10
start_minute = 45

end_hour = 24
end_minute = 9

print(f'I will finish the triathlon at {end_hour}:{end_minute:02}')


print('\n --- Exercise 3 --- ')

# You're going on a road trip. First, you drive to the local gas station to
# fill up your (practically empty) 12 gallon gas tank, at $3.04 per gallon.
# Then, you drive from Ithaca to Niagara Falls, a 164 mile trip, and back to
# Ithaca again. When you get back, you fill up your tank again until it is
# full, to compensate for the gas that you used. What is the total amount of
# money you spent on gas for this trip? Your car has a fuel economy of 46.3
# miles per gallon.

tank_size = 12
gas_price = 3.04
one_way_distance = 164
fuel_economy = 46.3

total_costs = 1.0

print(f'I will spend ${total_costs:.2f} in total on gas')


print('\n --- Exercise 4 --- ')

# You're hungry after your road trip, so you and your friends decide to make
# pancakes. You know that you have five eggs and 5oz of flour left at home.
# You look up a recipe, and it tells you that you need 1.5 cups of flour for
# one egg. A quick search reveals that 1 cup of flour is equivalent to 4.25oz.
# How much flour do you need to buy to use all of your eggs?

eggs = 5
flour_left = 5.0
cups_per_egg = 1.5
flour_oz_per_cup = 4.25

flour_to_buy = 1.0

print(f'I will need to buy {flour_to_buy:.2f}oz of flour')
