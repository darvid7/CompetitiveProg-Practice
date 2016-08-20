# correct :D

while(True):
	line = input().strip('\n')
	if line == "#":
		break

	size = len(line)
	check_size = (size-1)//2 -1

	can_do = False

	j = 0 # character to remove
	for i in range(len(line)):
		sample = line[:j] + line[j+1:]
		if len(sample)%2 == 0:	# even
			second_half = sample[len(sample)//2:]
		else:
			# odd
			second_half = sample[(len(sample)//2)+1:]
		if sample[:len(sample)//2] == second_half[::-1]:
			print(sample)
			can_do = True
			break
		j += 1
	if not can_do:
		print("not possible")

"""
	Instead of lists you can do this inplace
	- have 2 counters i from start, j from end

"""