"""
@author: David Lei
@since: 21/07/2016
@modified: 

1. Contigous subarray
2. Non-contigous subarray

contigous = sequential
"""


no_testcases = int(input())

def get_max_val_contigous(A):
    T = [0 for _ in range(len(A))]
    T[0] = A[0]
    for i in range(1,len(A)):
        T[i] = max(T[i-1]+A[i], A[i])
    return max(T)

def get_max_val_non_contigous(A):
    T = [0 for _ in range(len(A))]
    T[0] = A[0]
    for i in range(1, len(A)):
        T[i] = max(T[i-1], T[i-1]+A[i],A[i])
    return max(T)

for _ in range(no_testcases):
    no_ele = int(input())
    A = [int(a) for a in input().split(' ')]
    max_val_contigous = get_max_val_contigous(A)
    max_val_non_contigous = get_max_val_non_contigous(A)
    print(str(max_val_contigous) + ' ' + str(max_val_non_contigous))

