"""
@author: David Lei
@since: 24/07/2016
@modified: 

"""

s = str(input())

import itertools

combs = list(itertools.combinations(s, 4))
#print(combs)
total = 0
for c in combs:
    if c == c[::-1]:
        total += 1
# string[::-1] == reverse
print(total%(10**9+7))