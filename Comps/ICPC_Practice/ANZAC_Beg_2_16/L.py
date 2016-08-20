"""
@author: David Lei
@since: 13/08/2016
@modified: 

"""


while(True):
    alp = [0] * 26

    d = input()
    assume_valid = True
    if d == "END":
        break
    else:
        for c in d:
            if c == " ":
                pass
            else:
                index = abs(ord(c) - ord('A'))
                if alp[index] == 0:
                    alp[index] = 1
                else:
                    assume_valid = False
                    break
                    # invalid
        if assume_valid:
            print(d)


