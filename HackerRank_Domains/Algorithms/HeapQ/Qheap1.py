import heapq
n = int(input())
heap = []
for i in range(n):
    data = [int(x) for x in input().split(' ')]
    cmd = data[0]
    if cmd == 1: # add to heap
        heapq.heappush(heap,(data[1]))
    elif cmd == 2: # delete element from heap
        # print(heap)
        heap.remove(data[1])
        heapq.heapify(heap)
        """
        d = []
        for k in range(len(heap)):
            o = heapq.heappop(heap)
            if o == data[1]:
                break
            else:
                d.append(o)
        for e in d:
            heapq.heappush(heap, e)
        """
    else:
        # print(min(heap))
        v = heapq.heappop(heap)
        print(v)
        heapq.heappush(heap, v)