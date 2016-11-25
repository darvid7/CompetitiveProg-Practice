n = int(input())
heights = [int(x) for x in input().split(' ')]
table = []
soln = False
test_energy = 0
while(True):
    # print("Testing soln: "  + str(test_energy))
    traversed = 0
    energy = test_energy

    for i in range(0, len(heights)):

        if heights[i] > energy:
            gain = False
        elif heights[i] <= energy:
            gain = True

        if gain:
            # print("Gained")
            energy += (energy - heights[i])
        else:
            # print("Lost")
            energy -= (heights[i] - energy)

        traversed += 1
        # print("Test energy: " + str(energy))
        if energy < 0:
            break

        if traversed == len(heights):
            soln = True
            break
    if soln:
        print(test_energy)
        break
    else:
        # print("not soln: " + str(test_energy))
        test_energy += 1