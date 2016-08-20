no_mp = int(input())

action_items = {
    "S":10, "Q":5, "A":7,
    "L":-8, "F":4, "D":-5, "E":-10
}

class Mp:
    def __init__(self, number, first_name, last_name):
        self.num = int(number)
        self.name = str(first_name) + " " + str(last_name)
        self.points = 0

    def __lt__(self, other):
        if other.points > self.points:
            return True
        elif other.points == self.points:
            if other.num > self.num:
                return True
            else:
                return False
        return False
    def __gt__(self, other):
        if other.points < self.points:
            return True
        elif other.points == self.points:
            if other.num < self.num:
                return True
            else:
                return False
        return False
    def __eq__(self, other):
        if other.points == self.points:
            return True
        return False

Mps = {}

for i in range(no_mp):
    data = input().split(' ')
    new_mp = Mp(data[0], data[1], data[2])
    Mps[new_mp.num] = new_mp                # add new_mp to dict

action_entries = int(input())
for j in range(action_entries):
    data = input().split(" ")
    points = action_items[data[1]]
    mp = Mps[int(data[0])]                  # get mp
    mp.points += points                     # increment points

l = list(Mps.values())
l.sort()
max_value = max(l).points
min_value = min(l).points

# print max
maxi =[]

print(max_value, end=" ")
for mp in l[::-1]:
    if mp.points == max_value:
        #print(mp.name, end=" ")
        maxi.append(mp)
    else:
        break
maxi.sort()
for mp in maxi:
    print(mp.name, end= " ")

print("\n", end="")

mini = []
# print min
print(min_value, end=" ")
for mp in l:
    if mp.points == min_value:
        #print(mp.name, end=" ")
        mini.append(mp)
    else:
        break
mini.sort()
for mp in mini:
    print(mp.name, end=" ")
"""
 can specify comparitor function
arr.sort(cmp=)
"""