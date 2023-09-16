"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-09-11"
-------------------------------------------------------
"""
# Imports

# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


# constants
COSTLARGE = 75
COSTSMALL = 50
LargeDogs = int(input("Large dogs groomed"))
SmallDogs = int(input("Small dogs groomed"))
total = int(COSTLARGE*LargeDogs + COSTSMALL*SmallDogs)
print(f"Total earned for the day:${total}")
