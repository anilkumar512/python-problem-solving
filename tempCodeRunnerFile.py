percentage=float(input('Enter percentage:'))
if percentage>90:
    print('Grade is A')
elif 80<percentage<90:
    print('Grade is B')
elif 60<=percentage<=80:
    print('Grade is C')
elif percentage<60:
    print('Grade is D')