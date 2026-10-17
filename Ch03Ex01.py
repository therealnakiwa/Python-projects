LA = float(input(f'Enter length of rectangle A: '))
WA = float(input(f'Enter width of rectangle A: '))
LB = float(input(f'Enter length of rectangle B: '))
WB = float(input(f'Enter width of rectangle B: '))
area= LA * WA
brea= LB * WB
print(f'The Area of A is {area:.1f}')
print(f'The Area of B is {brea:.1f}')
if area > brea:
    print('Area A is greater than Area B.')
elif area < brea:
    print('Area B is greater than Area A.')
else:
    print('Area A is equal to Area B.')
