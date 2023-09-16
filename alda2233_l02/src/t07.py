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


Flyers = int(input("Number of flyers:"))
Volunteer = int(input("Number of volunteers:"))

Per_Voul = Flyers//Volunteer
Left = Flyers % Volunteer

print(f"Flyers per volunteer:{Per_Voul}")
print(f"Flyers left over: {Left}")
