num1=int(input('Enter a number1:'))
num2=int(input('Enter a number2:'))
operator=input("Enter option A.Addition B.Substraction C.Multiplication D.Division: E.Floor Division F.Remainder G.Power:")
match operator:
    case 'A': 
        print(num1+num2)
    case 'B': 
        print(num1-num2)
    case 'C':
        print(num1*num2)
    case 'D': 
        print(num1/num2)
    case 'E': 
        print(num1//num2)
    case 'F': 
        print(num1%num2)
    case 'G': 
        print(num1**num2)
    case _:
        print("Invalid option")

