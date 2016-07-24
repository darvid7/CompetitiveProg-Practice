"""
@author: David Lei
@since: 25/03/2016
@modified:

"""

class Case:
    def __init__(self,id):
        self.id = id
        self.data = None
        self.array = None
        self.int_value = None
        self.string_value = None

    def set_data(self, data):
        self.data = data

    def set_array(self, array):
        self.array = array

    def set_int_value(self, value):
        self.int_value = int(value)

    def set_string_value(self, value):
        self.string_value = str(value).strip("\n")

    def get_data(self):
        return self.data

    def get_array(self):
        return self.array

    def get_int_value(self):
        return self.int_value

    def get_string_value(self):
        return self.string_value

    def get_name(self):
        return "Case #" + str(self.id) + ": "

"""
Below 2 functions take in input of form '1 1515 1231 12' or 'abc edg assd' strip all newlines (\n)
then puts the item separated by a space into an array
"""

def string_input_to_array_ints(string_input):
    an_int = ""
    processed_input = []
    stripped_input = string_input.strip("\n")
    last_index = int(len(stripped_input))-1
    for char_index in range(len(stripped_input)):
        if stripped_input[char_index] == " ":
            an_int = int(an_int)
            processed_input.append(an_int)
            an_int = ""
        else:
            an_int += stripped_input[char_index]
        if char_index == last_index:
            an_int = int(an_int)
            processed_input.append(an_int)
            an_int = ""
    return processed_input

def string_input_to_array_str(string_input):
    a_string = ""
    processed_input = []
    stripped_input = string_input.strip("\n")
    last_index = int(len(stripped_input))-1
    for char_index in range(len(stripped_input)):
        if stripped_input[char_index] == " ":
            a_string = str(a_string)
            processed_input.append(a_string)
            a_string = ""
        else:
            a_string += stripped_input[char_index]
        if char_index == last_index:
            a_string = str(a_string)
            processed_input.append(a_string)
            a_string = ""
    return processed_input

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def read_input(size=None,path=None):
    if path:
        with open(path, "r") as file:
            read_data = file.readlines()
    elif size == 's':
        with open("A-small-practice.in", "r") as file:
            read_data = file.readlines()
    elif size == 'l':
        with open("A-lagre-practice.in", "r") as file:
            read_data = file.readlines()
    file.close
    try:
        number_cases = int(read_data[0])
    except ValueError:
        number_cases = (read_data[0])
    return number_cases, read_data


def write_output_direct(output_array):
    with open("output.txt", "w") as f:
        c = 1
        for i in output_array:
            f.write("Case #" + str(c) + ": " + str(i))
            f.write("\n")
            c+= 1
        f.close()


def write_output_listoflists(output_array, space=True):
    with open("output.txt", "w") as f:
        c = 1
        for i in output_array:
            f.write("Case #" + str(c) + ": ")
            for j in i:
                #print j
                f.write(str(j))
                if space:
                    f.write(" ")
            f.write("\n")
            c += 1
        f.close()

if __name__ == "__main__":
    pass