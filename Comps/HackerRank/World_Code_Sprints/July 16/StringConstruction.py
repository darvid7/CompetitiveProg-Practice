"""
@author: David Lei
@since: 24/07/2016
@modified: 

"""

import sys


n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    p =''
    t = 0
    for c in s:
        if c in p:
            p += c
        else:
            p += c
            t += 1

    print(t)