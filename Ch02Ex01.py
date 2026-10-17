# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 11:25:20 2026

@author: julia
"""

#ask projected sales
projected_sales= float(input(f'Enter the projected sales: '))
#function for projected profit
projected_profit = projected_sales * 0.18
#print the porfit

print(f'The projected profit is ${projected_profit:,.2f}')