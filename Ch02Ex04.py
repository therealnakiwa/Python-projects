# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 12:29:27 2026

@author: julia
"""

Charge_food = float(input(f'Enter the charge for food: \n'))
tip= Charge_food * 0.18
tax= Charge_food * .07
total= tax + tip + Charge_food
print(f'The Tip (18%) on the food charge of ${Charge_food:.2f} is ${tip:.2f}')
print(f'The Tax (7%) on the food charge of ${Charge_food:.2f} is ${tax:.2f}')
print(f'The Total amount, including Tax and Tip, is ${total:.2f}')