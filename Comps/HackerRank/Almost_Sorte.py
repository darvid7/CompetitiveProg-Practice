"""
@author: David Lei
@since: 13/08/2016
@modified: 

"""

n = int(input())

l = list(map(int, input().split(' ')))
can_rev = False
sorted = True
decending = 0
dec_start = None
dec_end = None


for i in range(len(l)-2):
    if l[i] <= l[i+1]:
        # sorted
        pass
    else:
        sorted = False

    if l[i] >= l[i+1]:
        # decending, can reverse
        if decending == 0:
            decending = 1
            if not dec_start:
                dec_start = i
                can_rev = True
    else:
        if decending == 1:
            dec_end = i
            decending = -1
        else:
            if decending == -1:
                can_rev = False