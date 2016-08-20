"""
@author: David Lei
@since: 13/08/2016
@modified: 

"""
def most_common(string):
    sols = []
    l = [0] * 26
    for c in string:
        if c == " ":
            pass
        else:
            idx = ord(c) - ord('A')
            l[idx] = l[idx] + 1     # count
    m = max(l)
    for i in range(len(l)):
        if l[i] == m:
            sols.append(chr(65+i))
    return sols

def min_dst_E(most_freq):
    if len(most_freq) > 1:
        return False
    e = ord('E')
    s = []
    ss = []
    for i in most_freq:
        dist = ord(i) - ord('E')
        s.append(abs(dist))
        ss.append(dist)
    idx = s.index(min(s))
    min_v = min(s)
    found = 0
    for i in s:
        if i == min_v:
            found += 1
            if found > 1:
                return False
    return ss[idx]

n = int(input())
for i in range(n):
    s = input()
    most_freq = most_common(s)


    min_dist = min_dst_E(most_freq)
    if min_dist:
        print(abs(min_dist), end = " ")
        new_s = ''
        for c in s:
            if c == " ":
                new_s += " "
            else:
                new_val = ord(c) - min_dist
                if new_val < 65:
                    new_val = 90 - (65 - new_val - 1)
                elif new_val > 90:
                    new_val = new_val%90 + 65
                new_s += chr(new_val)

        print(new_s)
    else:
        print("NOT POSSIBLE")