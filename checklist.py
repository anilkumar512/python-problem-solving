collection=eval(input('Enter a collection:'))
if type(collection)==list:
    print('This is a list')
if len(collection)%2==0:
    print('List contains even number of values')