"""
@author: David Lei
@since: 3/08/2016
@modified: 

"""

t = int(input())
for i in range(t):
    b = int(input())
    found = False
    arr = list(map(int, input().strip().split(" ")))
    sum_left = 0
    sum_right = sum(arr[1:])
    for j in range(1, len(arr)):
        sum_left += arr[j-1]
        sum_right -= arr[j]
        if sum_left == sum_right:
            found = True
            break

    if len(arr) == 1:
        found = True
    if found:
        print("YES")
    else:
        print("NO")