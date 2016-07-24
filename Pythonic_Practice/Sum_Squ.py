"""
@author: David Lei
@since: 1/04/2016
@modified:

Higher abstraction seems to be better (faster)

"""


def sum_sq(a,b):
    return a*a+b*b


def sum_sq_p(*a):                   # a is args
    return sum(x*x for x in a)      # list comprehension

if __name__ == "__main__":
    print(sum_sq(5, 4))           # 25 + 16
    print(sum_sq_p(5, 4))
    print(sum_sq_p(1, 2, 3, 4, 5, 6, 7))


