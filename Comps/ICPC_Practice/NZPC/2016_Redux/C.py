# correct :D

start_year = 1896

while(True):
	year = int(input().strip('\n'))

	if year == 0:
		break
	if year < 1896:
		s = "No summer games"
	elif (year - start_year) % 4 == 0: # year of games
		if year >= 1914 and year <= 1918: # world war 1
			s = "Games cancelled"
		elif year >= 1939 and year <= 1945: # world war 2
			s = "Games cancelled"
		elif year > 2020:
			s = "No city yet chosen"
		else:
			s = "Summer Olympics"
	else:
		s = "No summer games"
	print(str(year) + " " + str(s))