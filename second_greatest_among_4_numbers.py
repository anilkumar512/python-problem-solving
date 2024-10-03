num1=int(input('Enter num1:'))
num2=int(input('Enter num2:'))
num3=int(input('Enter num3:'))
num4=int(input('Enter num4:'))
if num1>num2:
    if num1>num3:
        if num1>num4:
            if num2>num3:
                if num2>num4:
                    print('num2 is second largest')
                else:
                     print('num4 is second largest')
            else:
                if num3>num4:
                     print('num3 is second largest')
                else:
                     print('num4 is second largest')
        else:
            print('num1 is second largest')
    else:
        if num3>num4:
           if num4>num2:
               if num4>num1:
                    print('num4 is second largest')
               else:
                    print('num1 is second largest')
           else:
                if num2>num1:
                     print('num2 is second largest')
                else:
                     print('num1 is second largest')
        else:
             print('num3 is second largest')
else:
    if num2>num3:
        if num2>num4:
            if num4>num1:
                if num4>num3:
                     print('num4 is second largest')
                else:
                     print('num4 is second largest')
            else:
                if num1>num3:
                    print('num1 is second largest')
                else:
                    print('num3 is second largest')
        else:
            print('num2 is second largest')
    else:
        if num3>num4:
            if num4>num1:
                if num4>num2:
                    print('num4 is second largest')
                else:
                    print('num2 is second largest')
            else:
                if num1>num2:
                    print('num1 is second largest')
                else:
                    print('num2 is second largest')
        else:
            print('num3 is second largest')
            
            
                

               