'''Happy Number
   Start with any positive integer.
   Replace the number with the sum of the squares of its digits.
   Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
   If it reaches 1, the number is considered a "happy number." Otherwise, it's not.
   Example: 
   number=19
   sum_of_squares=1^2 + 9^2 =82, 8^2 + 2^2 = 68, 6^2 + 8^2 =100, 1^2 + 0^2 + 0^2 =1, Since we reached 1, 19 is a happy number
   
   num = 20
   sum_of_squares = 2^2 + 0^2 = 4 , 4^2 = 16 , 1^2 + 6^2 = 1 + 36 = 37 , 3^2 + 7^2 = 9 + 49 = 58 , 5^2 + 8^2 = 25 + 64 = 89 .....
   Here we won't get 1 as sum_of_squares but the loop ends when we get a number that's already in the list.So,20 is not a happy number.

'''


number=int(input('Enter a number:'))
original_num=number
numbers=[]
while number != 1 and number not in numbers:
    numbers.append(number)
    sum_of_squares=0
    while number>0:
        digit=number%10
        sum_of_squares+=digit**2
        number//=10
    number=sum_of_squares
if number==1:
    print(f'{original_num} is a Happy Number')
else:
    print(f'{original_num} is not a Happy Number')