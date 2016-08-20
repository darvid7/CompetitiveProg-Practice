"""
@author: David Lei
@since: 13/08/2016
@modified: 

"""

import math
class Gorelian:
    def __init__(self, pos_x, pos_y, range):
        self.x = pos_x
        self.y = pos_y
        self.range = range
        self.radius = math.sqrt(range/math.pi)

Gs = []

def cry_out(G1, G2):

    x_diff = abs(G2.x - G1.x)
    y_diff = abs(G2.y - G1.y)
    merege = False
    if G1.range >= x_diff and G1.range >= y_diff:
        merege = True
    if G2.range >= x_diff and G2.range >= y_diff:
        merege = True

    if merege:
        meeting_point_x = float(G2.x + G1.x) / float(2)
        meeting_point_y = float(G2.y + G1.y) / float(2)
        new_range = G1.range + G2.range

        newG = Gorelian(meeting_point_x, meeting_point_y, new_range)
        return newG
    return False


no_gorelians = int(input())
for i in range(no_gorelians):
    data = list(map(int, input().split(' ')))
    new_gorelian = Gorelian(data[0], data[1], data[2])

    Gs.append(new_gorelian)

dropped = 1
for x in range(len(Gs)):
    for j in range(1, len( Gs)-1):

        try:

            res = cry_out(Gs[j], Gs[j-1])
            if res:
                a = Gs[j]
                b = Gs[j-1]
                Gs.remove(a)
                Gs.remove(b)
                Gs.insert(j, res)
        except IndexError:
            pass
print(len(Gs))