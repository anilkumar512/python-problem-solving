import math
n=int(input('Enter req multiple'))
val=int(input('Enter value'))
res=(math.ceil(val/n))*n
print('next',n,'th multiple for',val,'is',res)
