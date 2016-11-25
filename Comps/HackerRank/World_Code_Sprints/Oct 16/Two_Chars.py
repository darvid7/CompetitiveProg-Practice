"""
@author: David Lei
@since: 12/10/2016
@modified: 

"""

import sys
import itertools


s_len = int(input().strip())
s = [x for x in input().strip()]
dist_chars = set(s)
d = list(dist_chars)

perms = list(itertools.permutations(dist_chars, 2))

def test(perm_pair, s):
    dc = { perm_pair[0]:perm_pair[1],
            perm_pair[1]:perm_pair[0]}
    nextc = None
    l = 0
    for c in s:

        if c in perm_pair:
            if not nextc:
                nextc = dc[c]
                l += 1
            else:
                if c == nextc:
                    l += 1
                    nextc = dc[c]
                else:
                    return False
    return l
maxv = 0

for p in perms:
    res = test(p,s)
    # print(res)

    if res > maxv:
            maxv = res
            #print(pair)
print(maxv)