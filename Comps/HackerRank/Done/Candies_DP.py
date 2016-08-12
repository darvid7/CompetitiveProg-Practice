"""
@author: David Lei
@since: 2/08/2016
@modified:

passed !!

https://www.hackerrank.com/challenges/candies
"""

no_children = int(input())
children_ratings = []

for i in range(no_children):
    children_ratings.append(int(input()))

table = [1 for _ in range(no_children)]

if children_ratings[0] > children_ratings[1]:
    table[0] = table[1] + 1
if children_ratings[no_children-1] > children_ratings[no_children-2]:
    table[no_children-1] = table[no_children-2] + 1

for j in range(1, len(children_ratings)-1, 1):
    cur_child_rating = children_ratings[j]
    prev_child_rating = children_ratings[j-1]
    next_child_rating = children_ratings[j+1]

    if cur_child_rating > prev_child_rating and cur_child_rating > next_child_rating:
        table[j] = max(table[j-1], table[j+1]) + 1
    elif cur_child_rating > prev_child_rating:
        table[j] = table[j-1] + 1
    elif cur_child_rating > next_child_rating:
        table[j] = table[j+1] + 1
    else:
        pass

if children_ratings[0] > children_ratings[1]:
    table[0] = table[1] + 1
if children_ratings[no_children-1] > children_ratings[no_children-2]:
    table[no_children-1] = table[no_children-2] + 1

for j in range(len(children_ratings)-1-1, 0, -1):
    cur_child_rating = children_ratings[j]
    prev_child_rating = children_ratings[j-1]
    next_child_rating = children_ratings[j+1]

    if cur_child_rating > prev_child_rating and cur_child_rating > next_child_rating:
        table[j] = max(table[j-1], table[j+1]) + 1
    elif cur_child_rating > prev_child_rating:
        table[j] = table[j-1] + 1
    elif cur_child_rating > next_child_rating:
        table[j] = table[j+1] + 1
    else:
        pass


if children_ratings[0] > children_ratings[1]:
    table[0] = table[1] + 1
if children_ratings[no_children-1] > children_ratings[no_children-2]:
    table[no_children-1] = table[no_children-2] + 1

#for i in range(no_children-1-1):
 #   if children_ratings[i] > children_ratings[i+1] and table[i] <= table[i+1]:
  #      print(' -- wrong pair --')
   #     print(str(i) + ' => rating: ' + str(children_ratings[i]) + ', table value: ' + str(table[i]))
    #    print(str(i+1) + ' => rating: ' + str(children_ratings[i+1]) + ', table value: ' + str(table[i+1]))
     #   print('~~ wrong pair end ~~')

 #   print('i: ' + str(i) + ', rating: ' + str(children_ratings[i]) + ', table value: ' + str(table[i]))
#print(table)


print(sum(table))