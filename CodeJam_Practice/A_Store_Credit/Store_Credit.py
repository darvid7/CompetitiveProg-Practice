"""
@author: David Lei
@since: 24/03/2016
@modified:

Problem :https://code.google.com/codejam/contest/351101/dashboard#s=p0
Works!
"""
class Case:
    def __init__(self, id):
        self.case_id = id
        self.credit = None
        self.no_items = None
        self.item_costs = None
        self.soln = None

    def set_credit(self, credit):
        self.credit = credit

    def set_no_items(self, no_items):
        self.no_items = int(no_items)

    def set_item_costs(self, item_costs):
        self.item_costs = item_costs

    def show(self):
#        self.item_costs = eval(self.item_costs)
        print (self.item_costs)
        print (self.item_costs.__class__)
        print (self.item_costs[0])
        print (self.item_costs[0].__class__)

    def process_costs(self):
        processed_costs = []
        an_int = ""
        item_costs = self.item_costs.strip("\n")
        length = len(item_costs)
        last_index = int(len(item_costs))-1
        for char_index in range(len(item_costs)):
            if item_costs[char_index] == " ":
                an_int = int(an_int)
                processed_costs.append(an_int)
                an_int = ""
            else:
                an_int += item_costs[char_index]
            if char_index == last_index:
                an_int = int(an_int)
                processed_costs.append(an_int)
                an_int = ""
        self.item_costs = processed_costs

    def solve(self):
        found = False
        found_item1 = None
        found_item2 = None
        credit = int(self.credit)
        no_items = self.no_items
        costs = self.item_costs
        for i in range(int(self.no_items)):

            for j in range(int(self.no_items)):
                print ("i : " + str(i))
                print ("j : " + str(j))
                if i == j:
                    pass
                else:
                    cost1 = self.item_costs[i]
                    cost2 = self.item_costs[j]
                    added_cost = cost1+cost2    # self.item_costs[i] + self.item_costs[j]
                    if added_cost == int(self.credit):
                        found = True
                        found_item1 = i
                        found_item2 = j

                        if i < j:
                            return found_item1, found_item2
                        else:
                            return found_item2, found_item1
                jj = j
                print (str(jj) + ": " + str(j))

    def set_soln(self, index1, index2):
        self.soln = (index1+1, index2+1)

    def get_first_soln_index(self):
        return self.soln[0]
    def get_second_soln_index(self):
        return self.soln[1]




def read_input():
    with open("/Users/David/PycharmProjects/CodeJam_Practice/A_Store_Credit/sample.in", "r") as file:
        read_data = file.readlines()

    file.close
    return read_data

def main():
    import os
    print (os.getcwd())
    info = read_input()
    number_inputs = int(info[0])
    cases =  []
    for case in range(number_inputs):
        a_case = Case(case)
        cases.append(a_case)

    i = 1
    for case in cases:
        a_credit = info[i]
        case.set_credit(a_credit)
        i += 1
        a_num_items = info[i]
        case.set_no_items(a_num_items)
        i += 1
        a_item_costs = info[i]
        case.set_item_costs(a_item_costs)
        i += 1

    for case in cases:
        case.process_costs()
        case.show()

    for case in cases:
        solns = case.solve()
        case.set_soln(solns[0], solns[1])
    print (" SOLUTIONS ")

    output_array = []
    case_number = 1
    for case in cases:
        print (case.soln)

        an_output = "Case #" + str(case_number) + ": " + str(case.get_first_soln_index()) + " " + str(case.get_second_soln_index())
        output_array.append(an_output)
        case_number += 1

    save_output(output_array)

def save_output(output_array):
    with open("output.txt", "w") as f:
        for i in output_array:
            f.write(i)
            f.write("\n")
        f.close()

if __name__ == "__main__":
    import os
    print (os.getcwd())
    main()
    #read_input()