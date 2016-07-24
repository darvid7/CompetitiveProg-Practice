"""
@author: David Lei
@since: 21/07/2016
@modified: 

"""

data = input().split(' ')
t1 = int(data[0])
t2 = int(data[1])
n = int(data[2])
def fib_modified(n):
    t = [0 for x in range(n)]
    t[0] = t1
    t[1] = t2
    for i in range(2,len(t)):
        t[i] = t[i-2] + t[i-1]**2
    print(t)
    return t[n-1]
print(fib_modified(n))
