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


Hight = float(input("enter your height (m):"))
Weight = float(input("enter your weight (kg):"))
UpperBMI = int(input(
    "Enter your upper limit BMI (23 if you are from South East Asia and Southern China, 25 for everyone else):"))

BMI = Weight/Hight**2
BMIPrime = BMI/UpperBMI

print(f"Body Mass Index (kg/m^2) = {BMI}")
print(f"BMI Prime = {BMIPrime}")
