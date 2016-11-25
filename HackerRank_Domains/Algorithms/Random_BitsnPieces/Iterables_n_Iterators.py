"""
@author: David Lei
@since: 13/08/2016
@modified: 

"""
import itertools
n = int(input())
d = input().split(' ')
#print(d)
size = int(input())


combs = itertools.combinations(d, size)
have_a = 0
total_no = 0
for t in combs:
    for j in t:
        if j == 'a':
            have_a += 1
            break
    total_no += 1
v = float(have_a)/float(total_no)
print("%.4f" % v)
#print(list(combs))