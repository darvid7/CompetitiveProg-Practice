"""
@author: David Lei
@since: 12/10/2016
@modified: 

"""

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
d = {}
for v in c:
    if v in d:
        d[v] += 1
    else:
        d[v] = 1

i = list(d.items())
sell = 0
for t in i:
    if t[1] >= 2:
        sell += t[1] // 2
        # l[1] = l[1] % 2
print(sell)