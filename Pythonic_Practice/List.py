"""
@author: David Lei
@since: 11/07/2016
@modified: 

"""
a = ['Mew', 'Charizard']
b = ['Golduck', 'Abra']

# generator comprehension
print('Generator comprehension')
print('\n'.join(i + ' vs ' + j for i,j in zip(a,b)))

# list comprehension
print('\nList comprehension')
[print(i,'vs',j) for i,j in zip(a,b)]