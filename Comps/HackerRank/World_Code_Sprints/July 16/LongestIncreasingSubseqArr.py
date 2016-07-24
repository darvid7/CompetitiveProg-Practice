"""
@author: David Lei
@since: 24/07/2016
@modified: 

"""
import itertools
t = int(input())

def check(tup, lis_arr):
    first = lis_arr[0]
    temp = list(tup)
    check_arr = [first]
    try:
        first_index = temp.index(first)
        no = first
        for i in range(first_index, len(temp)):
            if temp[i] == no+1:
                check_arr.append(temp[i])
                no = temp[i]
        if check_arr == lis_arr:
            return True
        return False

    except ValueError:
        return False


for i in range(t):
    size, lis = [int(c) for c in input().split(' ')]
    lis_arr = [k for k in range(1,lis+1)]            # make array containing LIS

    process_these =[]
    combs = list(itertools.combinations_with_replacement(lis_arr, lis))
    for combo in combs:
        p = list(combo)
        proc = lis_arr + p
        process_these.append(proc)
    total_res = []
    for l in process_these:
        partial_res = list(itertools.permutations(l, size))
        for part in partial_res:
            if list(part) not in total_res:
                total_res.append(list(part))
   #for l in process_these:
   #     partial_res = list(itertools.combinations_with_replacement(l, size))
   #     for part in partial_res:
   #         if list(part) not in total_res:
   #             total_res.append(list(part))

    actual = []
    for t in total_res:
        if check(t, lis_arr):
            actual.append(t)

    #print(len(total_res))
    #print(total_res)
    print(len(actual))
    #print(actual)