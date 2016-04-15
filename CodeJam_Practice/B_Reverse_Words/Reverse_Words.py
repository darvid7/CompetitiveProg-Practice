"""
@author: David Lei
@since: 25/03/2016
@modified: 

Problem: https://code.google.com/codejam/contest/351101/dashboard#s=p1
Works!
"""
from CodeJam_lib.Input_lib import *

def main():
    number_cases, input_data = read_input(path="B-large-practice.in")

    cases = []
    i = 1
    for _ in range(number_cases):
        a_case = Case(i)
        processed_line = string_input_to_array_str(input_data[i])
        a_case.set_data(processed_line)
        i += 1
        cases.append(a_case)

    solns = [solve_case(case) for case in cases]

    write_output_listoflists(solns)

def solve_case(a_case):
    an_array_of_strings = a_case.get_data()
    soln = []

    for i in an_array_of_strings:
        soln.insert(0, i)

    return soln

if __name__ == "__main__":
    main()