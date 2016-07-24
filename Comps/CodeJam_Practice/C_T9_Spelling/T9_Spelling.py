"""
@author: David Lei
@since: 25/03/2016
@modified: 

Problem: https://code.google.com/codejam/contest/351101/dashboard#s=p2
Works!
"""

from CodeJam_lib.Input_lib import *

def main():
    number_cases, input_data = read_input(path="C-large-practice.in")

    decoder = {
               'A': 2, 'B': 22, 'C': 222,
               "D": 3, "E": 33, "F": 333,
               "G": 4, "H": 44, "I": 444,
               "J": 5, "K": 55, "L": 555,
               "M": 6, "N": 66, "O": 666,
               "P": 7, "Q": 77, "R": 777, "S": 7777,
               "T": 8, "U": 88, "V": 888,
               "W": 9, "X": 99, "Y": 999, "Z": 9999,
               " ": 0
               }
    cases = []
    i = 1
    for _ in range(number_cases):
        a_case = Case(i)
        processed_line = str(input_data[i]).strip("\n")
        a_case.set_data(processed_line)
        i += 1
        cases.append(a_case)

    solns = [solve_case(case, decoder) for case in cases]
    #print solns
    write_output_listoflists(solns, space=False)

def solve_case(a_case, decoder):
    a_string = a_case.get_data()
    soln = []
    prev = None
    added = 0
    for i in range(len(a_string)):
        value = decoder[a_string[i].upper()]
        soln.append(value)

        if prev == int(str(value)[0]):
            #print "i : " + str(i)
            #print "before : " + str(soln)
            soln.insert(i+added, " ")
            #print "after : " + str(soln)
            #print "prev : " + str(prev)
            #print "value : " + str(value)
            added += 1

        prev = int(str(value)[0])

    return soln

if __name__ == "__main__":
    main()