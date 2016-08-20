"""
@author: David Lei
@since: 13/08/2016
@modified: 

"""

n = int(input())

men = 0
women = 0

q = input()

Q = [x for x in q]

while(Q):
    if abs(men-women) <= n:

        if Q[0] == 'M':
            # try add man
            if abs((1+men)-women) <= n:
                men += 1
                Q.remove('M')
            # can't add man, try add women
            else:
                if Q[1] == 'W':
                    if abs(men-(women+1)) <= n:
                        women += 1
                        Q.remove('W')
                    else:
                        if abs(men-(women+1)) <= n:
                            women += 1
                        break
                else:
                    if abs((1+men)-women) <= n:
                        men += 1
                    break

        elif Q[0] == 'W':
            # try add women
            if abs(men-(1+women)) <= n:
                women += 1
                Q.remove('W')
                # can't add women, try add man
            else:
                if Q[1] == 'M':
                    if abs((men+1)-women) <= n:
                        men += 1
                        Q.remove('M')
                    else:
                        if abs((1+men)-women) <= n:
                            men += 1
                        break
                else:
                    if abs(men-(women+1)) <= n:
                        women += 1
                    break
    else:

        break

print(men+women)