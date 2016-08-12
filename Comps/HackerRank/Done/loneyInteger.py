"""
@author: David Lei
@since: 3/08/2016
@modified: 

"""


def lonelyinteger(b):
    # b is a lis
    b.sort()
    #print(b)
    found = False
    if len(b) > 1:

        for i in range(1,len(b)-2):
            if b[i] != b[i-1] and b[i] != b[i+1]:
                found = True
                print(b[i])
        if not found:
            if b[len(b)-1] != b[len(b)-2]:
                print(b[len(b)-1])

    else:
        print(b[0])
# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = list(map(int, input().strip().split(" ")))
    lonelyinteger(b)