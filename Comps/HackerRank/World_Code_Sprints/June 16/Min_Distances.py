"""
@author: David Lei
@since: 26/06/2016
@modified: 

"""

import sys

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

s = set(A)
same = []
for i in s:
    if A.count(i) > 1:
        same.append(i)
mini = -1
for j in same:
    l = []
    while(True):
        try:
            index = A.index(j)
            A[index] = 'd'
            l.append(index)
        except ValueError:
            break
    zipped = zip(l[:-1],l[1:])
    for z in zipped:
        v = abs(z[0]-z[1])
        if mini == -1:
            mini = v
        else:
            mini = min(v, mini)



print(mini)

