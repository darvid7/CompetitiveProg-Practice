"""
@author: David Lei
@since: 27/07/2016
@modified: 

"""

def pow(x,y):
    t = float(x)
    if y == 0:
        return float(1)
    t = pow(float(x), float(y//2))
    if y%2 == 0:
        return (float(t)*float(t))%1000000007
    else:
        if y>0:
            return (float(x)*float(t)*float(t))%1000000007
        else:
            return ((float(t)*float(t))//float(x))%1000000007

a_growth_factor, b_growth_factor, time = [int(c) for c in input().split(' ')]
k = pow(float(3), float(time-1))
l = float(0.5)
o = float(a_growth_factor)+float(b_growth_factor)
mods = 1000000007
p = (k*l*o)
print(int((p)))
#2 4 999999999
#1731803157.0