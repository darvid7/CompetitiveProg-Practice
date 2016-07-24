"""
@author: David Lei
@since: 26/06/2016
@modified: 

5 3 4
3 2 1 1 1
4 3 2
1 1 4 1

"""

import sys

n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
# n1, n2, n3 are no items in stack
# h1, h2, h3 is the stack
# sum h1, h2, h3 is height of stack
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

height_h1 = sum(h1)
height_h2 = sum(h2)
height_h3 = sum(h3)

while not height_h1==height_h2==height_h3:

    m = min(height_h1, height_h2, height_h3)


    while not height_h1<= m:
        height_h1 -= h1[0]
        del h1[0]

    while not height_h2<= m:
        height_h2 -= h2[0]
        del h2[0]

    while not height_h3<= m:
        height_h3 -= h3[0]
        del h3[0]

print(height_h1)