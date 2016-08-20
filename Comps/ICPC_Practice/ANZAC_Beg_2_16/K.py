"""
@author: David Lei
@since: 13/08/2016
@modified: 

"""
# ---
# ----- minHeap class to implement a priority Queue for dijkstra-----
class minHeap:
    '''
    a minHeap used to implement priority Queues
    the getMin operation will take the element at the root of the heap
    this will be sorted by path length
    thus vertex with shortest path will be returned
    '''
    def __init__(self):
        '''
        initialize count and array for heap
        @return:
        '''
        self.count = 0
        self.array = [None]
    #size
    def __len__(self):
        return self.count


    def swap(self, a, b):
        #print(self.count)

        self.array[a],self.array[b] = self.array[b], self.array[a]

    def is_empty(self):
        return self.count == 0
    #append
    def add(self, item):
        '''
        @param item:
        @return:
        '''
        if self.count + 1 < len(self.array):
            self.array[self.count+1] = item
        else:
            self.array.append(item)
        self.count += 1
        self.rise(self.count)

    def rise(self, k):
        '''
        rise item at index k to correct position
        note: parent of k at k//2
        @precondition: 1 <= k <= self.count
        @return:
        '''
        # use riseLoopCondition to deal with infinity string
        while k > 1 and self._riseLoopCondition(k):
            self.swap(k, k//2)
            k = k//2


    def _riseLoopCondition(self, k):
        # process the condition - self.array[k].dist< self.array[k//2].dist
        # so we can deal with INFINITY
        if self.array[k].dist == 'INFINITY':
                if self.array[k//2] == 'INFINITY':
                    return False
                    # both unknown, one not < other so dont loop
                else:
                    return False
                    # k//2 is known & is less than infinity (unknown)
                    # k is > k//2 so not k < k//2 to dont loop
        else:
            if self.array[k//2].dist == 'INFINITY':
                # k//2 > k, so k < k//2
                return True
            elif self.array[k].dist< self.array[k//2].dist:
                # both known and k<k//2
                return True
            else:
                return False


    # serve
    def getMin(self):
        '''
        # swap items at root and min
        #return self.array[1]
        '''
        try:
            self.swap(1, self.count)
            self.minItem = self.array[self.count]
            self.count -= 1 # delete item
            self.array.pop()
            self.sink(1)
            return self.minItem
        except IndexError:
            print("Nothing in the heap! ")

    def decreasedKey(self, itemDecreased,value):
        index = 0
        for i in self.array[1:]:
            index += 1
            if i.name == itemDecreased.name:
                vertex = i
                vertex.dist = value
                break
        #print('index')
        #print(index)

        #self.delete(index)
        #self.add(vertex)
        #self.swap(index, self.count)

        #self.sink(1)
        self.rise(index)
        '''
        index = 'string'
        for i in range(len(self.array)):
            if self.array[i] == itemDecreased:
                index = i
                break
        self.swap(index, self.count)
        self.sink(1)
        '''
    # make item k sink into correct position
    def sink(self, k):
        while 2*k <= self.count:
            child = self.smallest_child(k)
            if self._sinkComparisonCondition(k, child):
                break
            self.swap(child, k)
            k = child

    def _sinkComparisonCondition(self,k,child):
        '''
        process condition - self.array[k] <= self.array[child]
        '''
        #print(self.array[k].dist)
        #print(self.array[child].dist)
        if self.array[k].dist == 'INFINITY' and self.array[child].dist == 'INFINITY':
            # both equal dist, so break loop
            return True
        elif self.array[k].dist == "INFINITY":
            # k is > so never less, condition not met, so dont break
            return False
        elif self.array[child].dist == 'INFINITY':
            # child is either > or equal to k
            #  so k <= child, thus break
            return True
        # values are not infinity
        elif self.array[k].dist <= self.array[child].dist:
            # break
            return True
        else:
            # comparison condition not met, don't break
            return False



    def smallest_child(self,k):
        '''
        return the index of smallest child of K
        @precondition: 2*k <= self.count (has at least 1 child)
        @param k:
        @return:
        '''
        if 2*k == self.count or self._smallestChildCondition(k):
           return 2*k
        else:
            return 2*k+1

    def _smallestChildCondition(self,k):
        '''
        process condition - elf.array[2*k].dist < self.array[2*k+1].dists
        '''

        if self.array[2*k].dist == "INFINITY":
            # won't be smaller so condition not met
            # always bigger or = to 2*k+1
            # takes care of both > and = case
            return False
        elif self.array[2*k+1].dist == "INFINITY":
            # 2*k is not INFINITY
            # 2*k+1 is so
            # 2*k always < 2*k+1, thus condition met
            return True
        elif self.array[2*k].dist < self.array[2*k+1].dist:
            # both known and not INFINITY
            return True
        else:
            return False




    #print
    def __str__(self):
        return str(self.array[1:])



    def return_array(self):
        self.mirrage_array = []
        for item in self.array[1:]:
            self.mirrage_array.append(str(item))
        #print(self.mirrage_array)
        return self.mirrage_array

    def delete(self, k):
        if k > 0 and k < self.count:
            self.swap(k, self.count)
            self.count-=1
            self.array.pop()
            self.sink(k)
        else:
            pass

# ---

class Thing:
    def __init__(self, s, d):
        self.string = s
        self.dist = d
# ---

row1 = ['q','w','e','r','t','y','u','i','o','p']
row2 = ['a','s','d','f','g','h','j','k','l']
row3 = ['z','x','c','v','b','n','m']

def get_idx(a_char):
    row_idx = 0
    try:
        col_idx = row1.index(a_char)
        row_idx = 0
    except ValueError:
        try:
            col_idx = row2.index(a_char)
            row_idx = 1
        except ValueError:
            try:
                col_idx = row3.index(a_char)
                row_idx = 2
            except ValueError:
                pass
    return row_idx, col_idx

def distances_chars(char_typed, char_check):
    typed_row, typed_col = get_idx(char_typed)
    check_row, check_col = get_idx(char_check)
    return abs(check_row-typed_row) + abs(check_col-typed_col)


def distance_strs(str_typed, str_check):
    sum_dist = 0
    for i in range(len(str_typed)):
        dist = distances_chars(str_typed[i], str_check[i])
        sum_dist += dist
    return sum_dist

test_cases = int(input())

def print_min(store):
    while(store):
        min_dist = store[0][1]
        min_wrd = store[0][0]
        for i in range(1,len(store)):
            if store[i][1] == min_dist:
                min_wrd = min(min_wrd, store[i][0])
            elif store[i][1] < min_dist:
                min_dist = store[i][1]
                min_wrd = store[i][0]
        print(min_wrd + ' ' + str(min_dist))
        info = min_wrd, min_dist
        store.remove(info)

for i in range(test_cases):
    pq = minHeap()
    data = input().split(' ')
    typed = data[0]
    no_spellcker_list = int(data[1])
    for j in range(no_spellcker_list):
        entry = input()
        total_distance = distance_strs(typed, entry)
        thing = Thing(entry, total_distance)
        pq.add(thing)

    while(not pq.is_empty()):
        thing =  pq.getMin()
        print(thing.string + ' ' + str(thing.dist))





