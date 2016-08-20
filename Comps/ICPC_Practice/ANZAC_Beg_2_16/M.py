"""
@author: David Lei
@since: 13/08/2016
@modified: 

"""
d = list(map(int, input().split(' ')))
k = d[0]
d.remove(k)

c =1
for _ in range(d[0]):
    print(c, end=" ")
c += 1

for i in range(1,len(d)):

    for j in range(d[i]-d[i-1]):
        print(c, end=" ")
    c += 1


