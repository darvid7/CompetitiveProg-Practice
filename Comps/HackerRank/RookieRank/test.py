def pow(x,y):
    t = float(x)
    if y == 0:
        return float(1)%1000000007
    t = pow(float(x), float(y//2))
    if y%2 == 0:
        return (float(t)*float(t))%1000000007
    else:
        if y>0:
            return (float(x)*float(t)*float(t))%1000000007
        else:
            return ((float(t)*float(t))/float(x))%1000000007
print(pow(3,9000000))