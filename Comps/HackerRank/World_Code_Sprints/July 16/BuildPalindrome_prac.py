"""
@author: David Lei
@since: 25/07/2016
@modified: 

"""

times = int(input())
for i in range(times):
    a = str(input())
    b = str(input())



    temp = a[0]
    index = 0
    max_l = 0
    maxx = ''
    found = False
    for i in range(len(a)):
        if temp in b:
            found=True
            if len(temp) > max_l:
                maxx = temp
                max_l = len(temp)
            elif len(temp) == max_l:
                maxx = min(temp, maxx)
            if i+1 < len(a):
                temp = a[i+1] + temp
        else:
            temp = temp[:-1]

            if temp in b:
                if len(temp) > max_l:
                    maxx = temp
                    max_l = len(temp)
                elif len(temp) == max_l:
                    maxx = min(temp, maxx)
            if i+1 < len(a):
                temp = a[i+1] + temp
    if not found:
        print('-1')
    else:
        #print(maxx)
        res = maxx[::-1]
        first_index_b = b.find(maxx)
        last_index_b = b.find(maxx[-1], first_index_b)

        first_index_a = a.find(res)
        last_index_a = a.find(res[-1], first_index_a)

        if first_index_b == 0 and last_index_a < len(a)-1:
            extra = a[last_index_a+1]# from a
        else:
            extra = b[first_index_b-1] # from b

        pal = a[first_index_a:last_index_a+1] + extra + b[first_index_b:last_index_b+1]

        print(pal)
