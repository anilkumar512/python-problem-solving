rows=int(input('Enter number of rows:'))
columns=int(input('Enter number of columns:'))
for row in range(rows):
    for col in range(columns):
        print((row,col),end=" ")
    print()


rows=int(input('Enter number of rows:'))
columns=int(input('Enter number of columns:'))
matrix=[]
for row in range(rows):
    matrix.append([])
    for col in range(columns):
       value=int(input(f'Enter value for matrix[{row,col}]:'))
       matrix[row].append(value)
# print(matrix)
for index in range(len(matrix)):
    print(matrix[index])


rows=int(input('Enter number of rows:'))
columns=int(input('Enter number of columns:'))
for row in range(rows):
    for col in range(columns):
        if row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


rows=int(input('Enter number of rows:'))
columns=int(input('Enter number of columns:'))
for row in range(rows):
    for col in range(columns):
        if col==0 or row==(rows-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


rows=int(input('Enter number of rows:'))
columns=int(input('Enter number of columns:'))
for row in range(rows):
    for col in range(columns):
        if row==0 or col==0 or row==(rows-1) or col==(columns-1) or row==(rows-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()