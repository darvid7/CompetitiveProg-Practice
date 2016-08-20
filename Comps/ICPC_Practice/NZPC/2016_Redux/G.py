# correct :D

def binary_search_iterative(n):
    target = n
    arr = [x for x in range(1, 51)]
    high = 49
    low = 0

    while(low <= high):
        mid = (high + low)//2

        s = arr[mid]
        #print(arr[low:high])
        print(s, end =" ")

        if target == arr[mid]:
            return arr[mid]
        else:
            if target > arr[mid]:
                low = mid +1
            elif target < arr[mid]:
                high = mid -1


#binary_search_iterative(1)

while(True):

   n = int(input())
   if n == 0:
       break
   binary_search_iterative(n)
   print("\n", end="")

