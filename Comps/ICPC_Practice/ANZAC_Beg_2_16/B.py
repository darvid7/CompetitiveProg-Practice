"""
@author: David Lei
@since: 13/08/2016
@modified: 

"""
class Player:
    def __init__(self, name):
        self.name = name
        self.ships = []
    def has_ships_left(self):
        if self.ships:
            return True
        return False
    def ship_hit(self, x, y):
        try:
            cord = (x,y)
            self.ships.remove(cord)
            return  True
        except ValueError:
            return False



d = (list(map(int, input().split(' '))))
width = d[0]
height = d[1]
no_shots = d[2]

#p1 = [['-' for x in range(height)] for _ in range(width)]
#p2 = [['-' for x in range(height)] for _ in range(width)]
p1 = Player('1')
p2 = Player('2')

for i in range(height):
    d = input()
    for w in range(width):
        if d[w] == '#':
            cord = (i,w)
            p1.ships.append(cord)
for i in range(height):
    d = input()
    for w in range(width):
        if d[w] == '#':
            cord = (i,w)
            p2.ships.append(cord)

player1_turn = True
player2_turn = False

for j in range(no_shots):
    #print(player1_turn)
    d = list(map(int, input().split(' ')))
    col = d[0]
    row = abs(d[1] - (height-1))
    if player1_turn:
        p1_hit = p2.ship_hit(row, col)
        if p1_hit:
            if not p2.has_ships_left():
                player1_turn = False
                player2_turn = True

        else:
            player1_turn = False
            player2_turn = True
    else:

        p2_hit = p1.ship_hit(row, col)
        if p2_hit:
            if not p2.has_ships_left():
                player1_turn = False
                player2_turn = True
        else:
            player2_turn = False
            player1_turn = True

if p1.has_ships_left() and p2.has_ships_left():
    print("draw")
elif not p1.has_ships_left() and not p2.has_ships_left():
    print("draw")
elif p1.has_ships_left():
    print("player one wins")
elif p2.has_ships_left():
    print("player two wins")
#print(p1.ships)
#print(p2.ships)