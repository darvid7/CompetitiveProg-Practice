"""
@author: David Lei
@since: 10/07/2016
@modified: 

"""
import heapq

min_heap = []

no_cookies, sweetness = list(map(int, str(input()).split()))
cookies = list(map(int, str(input()).split()))

def new_sweetness(a,b):
    return 1*a + 2*b

count = 0

[heapq.heappush(min_heap, nx) for n in cookies]
if no_cookies % 2 == 0:
    go_to = no_cookies
else:
    go_to = no_cookies-1
for i in range(go_to):
    min_a = heapq.heappop(min_heap)
    if min_a >= sweetness:
        break
    elif len(min_heap) <1:
        break
    else:
        count += 1
        min_b = heapq.heappop(min_heap)
        heapq.heappush(min_heap, new_sweetness(min_a, min_b))
        #print(cookies)
if min_a >= sweetness:
    print(count)
else:
    print('-1')



# list(map(int, a))
# [int(c) for c in a]
# same