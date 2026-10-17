# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 13:02:42 2026

@author: julia
"""

miles_driven= float(input(f'Enter the miles driven: '))
gallons_used= float(input(f'Enter the gallons of fuel used: \n'))
mpg= miles_driven / gallons_used
print(f'Your Miles Per Gallon is {mpg:.1f}.')