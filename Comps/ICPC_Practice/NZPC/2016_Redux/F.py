# correct :D

s = int(input())

arr =[0]*26

def find_idx(char):
    return ord(char)-ord('A')

allocation = ""

for i in range(s):
    string = input()
    for char in string:
        if ord(char) >= 65 and ord(char) <= 90:
            idx = find_idx(char)
            #print(idx)
            if arr[idx] == 0:
                arr[idx] = 1
                allocation += char
print(allocation)
