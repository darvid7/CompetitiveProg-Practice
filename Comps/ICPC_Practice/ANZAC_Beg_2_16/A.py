"""
@author: David Lei
@since: 13/08/2016
@modified: 

"""

d = list(map(int, input().split(' ')))
a = d[0]
b = d[1]

print(str(a) + ' * ' + str(b) + ' = ' + str(a*b))
if b == 0:
    print(str(a) + ' / ' + str(b) + ' is an ILLEGAL OPERATION' )
else:
    print(str(a) + ' / ' + str(b) + ' = ' + str(a//b) + ' remainder ' + str(a%b))

