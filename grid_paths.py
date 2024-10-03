'''Give the no.of unique paths from the top left corner to bottom right corner of grid
Constraint: You can move down right/down 1 unit at a time
'''

def grid_paths(rows,cols):
    if rows == 1 or cols == 1:
        return 1
    else:
        return grid_paths(rows-1,cols)+grid_paths(rows,cols-1)

rows=int(input('Enter number of rows of grid:'))
cols=int(input('Enter number of cols of grid:'))
paths=grid_paths(rows,cols)
print(f'The no of unique paths:{paths}')

    