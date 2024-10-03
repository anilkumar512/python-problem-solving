value=eval(input('Enter a value:'))
if value in [0,0.0,0+0j,False,[],(),set(),{}]:
    print('Entered value is default value...')