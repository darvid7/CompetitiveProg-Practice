"""
@author: David Lei
@since: 10/07/2016
@modified: 

- O(N3) Folyd Warshall
- O(N3) Matrix Mult
- Edit Distance
"""

def fib(n):
    t = [0]*n
    t[0] = 1
    t[1] = 1
    for i in range(2, n):
        t[i] = t[i-1] + t[i-2]
    return t[n-1]

print(fib(19))

