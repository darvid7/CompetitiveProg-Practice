"""
@author: David Lei
@since: 25/07/2016
@modified: 

"""

size = int(input())
arr = [int(c) for c in input().split(' ')]

def insertion_sort(arr):

    for i in range(1,len(arr)):
        temp = arr[i]
        j = i - 1
        shifted = False
        while j >= 0 and arr[j] >  temp:
            arr[j+1] = arr[j]
            j -= 1
            [print(x, end=" ") for x in arr]
            print('\n', end="")
            shifted = True
        arr[j+1]=temp
        if shifted:
            [print(x, end=" ") for x in arr]
            print('\n', end="")
insertion_sort(arr)

