"""
@author: David Lei
@since: 27/07/2016
@modified: 

"""

no_steps = int(input())
steps = input()
# start @ sea lvl

mountain = False
valley = False

first = steps[0]

level = 0

if first == 'U':
    mountain = True
    level += 1
else:
    valley = True
    level -= 1

v = 0

for i in range(1,len(steps)):
    if steps[i] == 'U':
        if mountain:
            if level == 0:
                mountain = True
                valley = False
            level += 1
        else:
            level += 1
            if level == 0:
                v += 1
                valley = False
                mountain = True
    else:
        if mountain:
            if level == 0:
                mountain = False
                valley = True
            level -= 1
        else:
            level -= 1


print(v)



