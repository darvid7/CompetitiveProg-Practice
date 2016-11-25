# both correct :D
# sort list less efficient but easier to read and debug


n = int(input().strip('\n'))
"""
l = []

for i in range(n):
	number = float(input().strip('\n'))
	l.append(number)

l.sort()

#print(l)

"""
cheapest = None
second_cheapest = None

for i in range(n):
	number = float(input().strip('\n'))

	assigned = False

	if not second_cheapest:
		if not cheapest:
			cheapest = number
			assigned = True
		else:
	
			second_cheapest = number
			#assigned = True

	if not assigned:
		if number < cheapest:
			second_cheapest = cheapest
			cheapest = number
		elif number < second_cheapest:
			second_cheapest = number
print("%.2f" % second_cheapest)
