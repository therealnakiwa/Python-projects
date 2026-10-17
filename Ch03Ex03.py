# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 12:33:41 2026

@author: julia
"""

num = int(input("Enter an integer from 1 - 20: "))

if num < 1 or num > 20:
    print("Error: Invalid Number")
else:
    if num == 1:
        roman = "I"
    elif num == 2:
        roman = "II"
    elif num == 3:
        roman = "III"
    elif num == 4:
        roman = "IV"
    elif num == 5:
        roman = "V"
    elif num == 6:
        roman = "VI"
    elif num == 7:
        roman = "VII"
    elif num == 8:
        roman = "VIII"
    elif num == 9:
        roman = "IX"
    elif num == 10:
        roman = "X"
    elif num == 11:
        roman = "XI"
    elif num == 12:
        roman = "XII"
    elif num == 13:
        roman = "XIII"
    elif num == 14:
        roman = "XIV"
    elif num == 15:
        roman = "XV"
    elif num == 16:
        roman = "XVI"
    elif num == 17:
        roman = "XVII"
    elif num == 18:
        roman = "XVIII"
    elif num == 19:
        roman = "XIX"
    else:       # num == 20
        roman = "XX"

    print(f"The Roman numeral for {num} is {roman}")
