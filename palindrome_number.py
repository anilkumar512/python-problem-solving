num=int(input('Enter number:'))
temp=num
rev=0
while num!=0:
    last_digit=num%10
    rev=rev*10+last_digit
    num=num//10
if rev==temp:
    print(f"The number {temp} is a palindrome")
else:
    print(f"The number {temp} is not a palindrome")