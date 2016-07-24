"""
@author: David Lei
@since: 10/07/2016
@modified:

Edit Distance
 - p = previous
    | a     | b     | c     | e     |
 a  | a=a, 0| p+b, 1| p+c, 2| p+e, 3|
 i  | p+i, 1| i=b, 1| p+c, 2| p+e, 3|
 f  | p+f, 2| p+f, 2| f=c, 2| p+e, 3|
edit_distance(abce, aif) = 3

 * = ab (top) to ai (left), easiest way is to replace b with i = 1 operation,
 other way is to remove b and add i which is 2 operations ab-b+i.


 acb & acd -> replace b with d = cost 1
 a & a -> replace a with a = cost 0
 ab & abc -> insert c or delete c = cost 1
 ab & aib -> insert i or delete i = cost 1

 Recurrence relation for i,j => 1 (after first row and col)
  Table[i][j] = min(top-left, top, left) + 1
"""

def edit_distance(string_a, string_b):
    t = [[0 for z in range(len(string_a))] for y in range(len(string_b))]
    if string_a[0] == string_b[0]:      # index[0][0]
        t[0][0] = 0
    else:
        t[0][0] = 1

    for i in range(1, len(string_a)):   # first row
        t[0][i] = t[0][i-1] + 1
    for j in range(1, len(string_b)):   # first col
        t[j][0] = t[j-1][0] + 1

    for h in range(1, len(string_a)):  # rows first
        for k in range(1, len(string_b)):  # then cols
            if string_a[h] == string_b[k]:
                cost = 0
            else:
                cost = 1    # not same, need operations
            if k==0 and h==0:
                t[k][h] = cost
            elif k>0 and h>0:
                c = min(t[k-1][h-1], t[k-1][h], t[k][h-1]) + cost
                t[k][h] = c
            elif k == 0:
                t[k][h] = t[k][h-1] + cost
            else:
                t[k][h] = t[k-1][h] + cost
    for l in t:
        print(l)
    print(t[len(string_b)-1][len(string_a)-1])
edit_distance('kaoffasfasdaaefazai','bagmziokkkpqjki')


from numpy import zeros

def edDistDp(x, y):
    """ Calculate edit distance between sequences x and y using
        matrix dynamic programming.  Return distance. """
    D = zeros((len(x)+1, len(y)+1), dtype=int)
    D[0, 1:] = range(1, len(y)+1)
    D[1:, 0] = range(1, len(x)+1)
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            delt = 1 if x[i-1] != y[j-1] else 0
            D[i, j] = min(D[i-1, j-1]+delt, D[i-1, j]+1, D[i, j-1]+1)
    print(D)
    print(D[len(x), len(y)])
    return D[len(x), len(y)]

edDistDp('kaoffasfasdaaefazai','bagmziokkkpqjki')

