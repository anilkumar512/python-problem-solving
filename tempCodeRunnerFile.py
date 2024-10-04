rows=int(input('Enter number of rows:'))
columns=int(input('Enter number of columns:'))
for row in range(rows):
    for col in range(row+1,columns):
        print(row*"*")
    print()
