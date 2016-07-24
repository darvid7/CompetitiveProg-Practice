"""
@author: David Lei
@since: 24/07/2016
@modified: 

"""
times = int(input())
for i in range(times):
    a = str(input())
    b = str(input())

    if len(a) <= len(b):
        shorter = a
        longer = b
    else:
        shorter = b
        longer = a


    temp = shorter[::-1]
    found = False
    for i in range(len(shorter)):
        if temp in longer:
            found = True
            break
        else:
            temp = temp[1:]
    if not found:
        print('-1')
    else:


        first_index = longer.find(temp)
        last_index = longer.find(temp[-1], first_index)
        pal = longer[first_index:last_index+2] + temp[::-1]

        print(pal)
