'''Perfect Number
A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself. 
For example, 28 is a perfect number because the divisors of 28 (excluding 26 itself) are 1, 2, 4,7,14 
and the sum of these divisors is 1 + 2 + 4 + 7+ 14 =28
So 28 is a Perfect Number
'''

number=int(input('Enter a number:'))
sum_of_factors=0
for factor in range(1,number):
    if number%factor==0:
        sum_of_factors+=factor
if sum_of_factors==number:
    print(f'{number} is a Perfect Number')
else:
    print(f'{number} is not a Perfect Number')

