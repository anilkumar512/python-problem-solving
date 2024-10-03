side_1=float(input('Enter side1:'))
side_2=float(input('Enter side2:'))
side_3=float(input('Enter side3:'))
if side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_3 + side_1 > side_2:
    if side_1 == side_2 == side_3:
        print('Equilateral triangle')
    else:
        if side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
            print('Isosceles triangle')
        else:
             print('Scalene triangle')          
else:
    print('Not a triangle')  
       