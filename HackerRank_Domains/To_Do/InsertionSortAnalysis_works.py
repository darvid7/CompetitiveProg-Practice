"""
taken from a post
go through with my soln
decompose & write iterative to solve
"""
def sort_and_count(arr, lo, hi):
    if hi - lo < 2:
        return 0

    mid = lo + ((hi - lo) >> 1)

    cnt_a = sort_and_count(arr, lo, mid)
    cnt_b = sort_and_count(arr, mid, hi)
    cnt_ab = merge_and_count(arr, lo, mid, hi)

    return cnt_a + cnt_b + cnt_ab



def merge_and_count(arr, lo, mid, hi):
    inversions = 0

    i, j = lo, mid
    temp_arr = []
    for k in xrange(hi - lo):
        if i >= mid:
            temp_arr.append(arr[j])
            j += 1
        else:
            if j >= hi:
                temp_arr.append(arr[i])
                i += 1
            elif arr[i] > arr[j]:
                inversions += (mid - i)
                temp_arr.append(arr[j])
                j += 1
            else:
                temp_arr.append(arr[i])
                i += 1

    index = lo
    while index < hi:
        arr[index] = temp_arr[index - lo]
        index += 1

    return inversions


T = input()
for iterate in xrange(T):
    n = input()
    q = [ int( i ) for i in raw_input().strip().split() ]
    answer = 0
    # Write code to compute answer using x, a and answer
    
    answer = sort_and_count(q, 0, n)
    
    print answer