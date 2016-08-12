"""
@author: David Lei
@since: 28/07/2016
@modified: 

"""

def merge_sort_aux(arr):
    total = []
    res = merge_sort(arr, total)
    print(len(total))
    return res


def merge_sort(arr, total):
    l = len(arr)
    if l <= 1:
        return arr
    else:
        mid = l//2
        left = merge_sort(arr[:mid], total)
        right = merge_sort(arr[mid:], total)
        partial_res = merge_lists(left, right, total)
        return partial_res

def merge_lists(a,b, total):
    result = []
    idx_a, idx_b = 0, 0
    len_a = len(a) - 1
    len_b = len(b) - 1
    invs_right = 0
    invs_left = 0
    while idx_a<=len_a or idx_b<=len_b:
        if idx_a > len_a:
            for i in range(idx_b, len_b+1):
                result.append(b[i])
            break
        elif idx_b > len_b:
            for i in range(idx_a, len_a+1):
                result.append(a[i])
                invs_left += 1
            break
        elif a[idx_a] <= b[idx_b]:
            result.append(a[idx_a])
            idx_a += 1
            #total.append(1)
        else:
            result.append(b[idx_b])
            idx_b += 1
            invs_right += 1
            #total.append(1)
    t = invs_right*invs_left + invs_right
    for _ in range(t):
        total.append(1)
    return result

#print(merge_sort_aux([2,1,3,1,2]))

cases = int(input())
for c in range(cases):
    no = int(input())
    data = [int(d) for d in input().strip(' ').split(' ')]
    merge_sort_aux(data)
