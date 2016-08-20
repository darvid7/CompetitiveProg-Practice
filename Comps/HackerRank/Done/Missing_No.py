"""
@author: David Lei
@since: 12/08/2016
@modified:
7251 7259 7276 7279 7292 7293
"""
a = {}
b = {}
no_a = int(input())
a_data = list(map(int, input().split(' ')))
no_b = int(input())
b_data = list(map(int, input().split(' ')))

for n in a_data:
    try:
        a[n] = a[n] + 1
    except KeyError:
        a[n] = 1

for n in b_data:
    try:
        b[n] = b[n] + 1
    except KeyError:
        b[n] = 1
ans = []

for i in set(b_data):
    if a[i] == b[i]:
        pass
    else:

       ans.append(i)

for k in ans:
    print(k, end=" ")

