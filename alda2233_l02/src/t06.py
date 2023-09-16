"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-09-16"
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


Mortgage = float(input("Mortgage principal amount ($)"))
Years = int(input("Number of years:"))
YIntrest = float(input("Yearly interest rate (%):"))

months = Years*12
MIntrest = YIntrest/(12*100)

Numerator = MIntrest*(1+MIntrest)**months
Denomenator = (1+MIntrest)**months-1
payment1 = Mortgage*(Numerator/Denomenator)


print(f"The monthly payments are:${payment1}")
