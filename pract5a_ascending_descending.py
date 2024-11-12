released={'Python 3.6':2017,'Python 1.0':2002,'Python 2.3':2010}
print('Original Dictionary:',released)
print('Dictionary in Ascending Order by Value:')
for key,value in sorted(released.items()):
    print(key,value)
print('Dictionary in descending Order by Value:')
for key,value in sorted(released.items(),reverse=True):
    print(key,value)
