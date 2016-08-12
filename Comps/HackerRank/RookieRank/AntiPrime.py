"""
@author: David Lei
@since: 27/07/2016
@modified: 

Formally, a positive integer  is antiprime if and only if it has more
divisors than any other positive integer smaller than n
"""

def get_factors(n):
    facs = 0
    for i in range(1, n+1//2):
        if n%i == 0:
            facs += 1
    return facs + 1

num = int(input())
st = ''
for i in range(num):
    q = int(input())
    max_facs = 0

    for j in range(1,q):
        f = get_factors(j)
        if f > max_facs:
            max_facs = f
    new_facs  = get_factors(q)
    while new_facs < max_facs:
        q += 1
        new_facs = get_factors(q)
    st += str(q) + '\n'
print(st)
