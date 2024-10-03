'''Function that counts the no of ways you can partition n objects using  parts upto m (m>=0)'''
def count_partitions(objects, parts):
    if objects==0:
        return 1
    elif parts==0 or objects<0:
        return 0
    else:
        return count_partitions(objects, parts-1) + count_partitions(objects-parts, parts)
objects=int(input('Enter no of objects:'))
parts=int(input('Enter no of parts:'))
partitions=count_partitions(objects,parts)
print(f'The no of partitions possible are:{partitions}')