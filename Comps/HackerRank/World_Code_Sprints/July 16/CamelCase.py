"""
@author: David Lei
@since: 24/07/2016
@modified: 

"""
import sys

p=0
s = input().strip()
for c in s:
    if c.isupper():
        p += 1
print(p+1)
