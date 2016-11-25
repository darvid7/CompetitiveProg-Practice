"""
@author: David Lei
@since: 11/07/2016
@modified: 

"""
# failed ;(
def find_next(n):
    # note: check by converting to str and checking last 0 as they are returned as floats
    if n == 1 or n == 2:
        return n-1
    elif str(n**0.5)[-1] == '0':     # has a square root i.e. 25**0.5 = 5
        return int(n**0.5)
    elif str(n/2)[-1] == '0':      # divides by 2 evenly i.e. 6/2 = 3
        return int(max(2, n/2))
    else:
        return n-1

queries = int(input())
for i in range(queries):
    num = int(input())
    c = 0
    while num != 0:
        num = find_next(num)
        c += 1
        print('turn: ' + str(c))
        print(num)
    print(c)




