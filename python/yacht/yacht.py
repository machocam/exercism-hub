"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
from collections import Counter 

# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    dice_count = dict(Counter(dice))

    # For YACHT
    if category == 0: 
        for die in dice_count: 
           if dice_count[die] == 5: 
               return 50
           else: 
               return 0

    # For single dies 
    if category in range(1, 7): 
        if category in dice: 
            return dice_count[category]*category
        else:
            return 0

    # For Full-House
    if category == 7:
        if 2 in dice_count.values() and 3 in dice_count.values():
            return sum(dice)
        else:
            return 0

    # Four of a kind 
    if category == 8: 
        if max(dice_count.values()) >= 4:
            return 4*list(dice_count)[list(dice_count.values()).index(max(dice_count.values()))]
        else: 
            return 0

    # Little straight 
    if category == 9: 
        if sorted(dice) == [1,2,3,4,5]:
            return 30 
        else:
            return 0

    # Big straight 
    if category == 10: 
        if sorted(dice) == [2,3,4,5,6]: 
            return 30 
        else:
            return 0

    # Choice 
    if category == 11: 
        return sum(dice)
