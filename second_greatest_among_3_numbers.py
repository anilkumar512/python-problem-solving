num1=int(input('Enter num1:'))
num2=int(input('Enter num2:'))
num3=int(input('Enter num3:'))
if num1>num2:
    if num1>num3:
        if num2>num3:
            print('num2 is Second Greatest')
        else:
            print('num3 is Second Greatest')
    else:
        print('num1 is Second Greatest')
else:
    if num2>num3:
        if num1>num3:
            print('num1 is Second Greatest')    
        else:
            print('num3 is Second Greatest') 
    else:
        print('num2 is Second Greatest')

