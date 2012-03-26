#!/usr/bin/env python

from random import randint
from math import ceil

def roll_dice_query(num_sides):
    try:
        num_dice = int(raw_input("How many dice? " ))
        print "-------------"
        for i in range(num_dice):
            print randint(1, 6),
        # print "\n"
    except ValueError:
        print "Please enter an integer."

while True:
    roll_dice_query(6)
