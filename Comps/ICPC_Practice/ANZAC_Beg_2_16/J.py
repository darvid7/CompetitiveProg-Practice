"""
@author: David Lei
@since: 13/08/2016
@modified: 

"""

mirs = {
    'b':'d',
    'd':'b',
    'p':'q',
    'q':'p',
    'i':'i',
    'o':'o',
    'v':'v',
    'w':'w',
    'x':'x'

}
d = input()
f = True
s = ''
for c in d:
    try:
        mir_c = mirs[c]
        s += mir_c
    except KeyError:
        print("INVALID")
        f = False
        break
if f:
    print(s[::-1])
