# Learn REG EX!
# do it the smart way
# my way doesn't work..
import re

fp = file("A-small-practice.in")
(l, d, n) = [int(x) for x in fp.next().split()]
words_in_lang = [fp.next() for x in range(d)]
print "words in lang : " + str(words_in_lang)
for i in range(1,n+1):
    search_string = fp.next().replace("(", "[").replace(")", "]")
    print "search_string : " + str(search_string)

    search_it = re.compile(search_string).search
    print "search_it : " + str(search_it)

    results = filter(search_it, words_in_lang)

    found = len(results)

    print "results : " + str(results)
fp.close()

"""
@author: David Lei
@since: 25/03/2016
@modified: 

Problem: https://code.google.com/codejam/contest/90101/dashboard#s=p0

I messed up - do string permutations first
this fries my comp

from CodeJam_lib.Input_lib import *

def main():
    ldn, input_data = read_input(path="A-small-practice.in")
    ldn = string_input_to_array_ints(ldn)
    l = int(ldn[0])                              # every word consists of exactly L lowercase letters
    d = int(ldn[1])                              # exactly D words in this language
    n = int(ldn[2])                              # no test cases

    words_in_lang = []
    for i in range(1,d+1, 1):
        a_word = input_data[i]
        processed_word = string_input_to_array_str(a_word)
        words_in_lang.append(processed_word[0])

    cases =[]
    case_no = 1
    for j in range(d+1, n+d+1, 1):
        a_case = Case(case_no)
        case_no += 1
        a_case.set_data(string_input_to_array_str(input_data[j]))
        cases.append(a_case)

    solns = [solve_case(case.get_data(), l, words_in_lang) for case in cases]
    #print solns
    write_output_direct(solns)

def solve_case(a_case_data, l, words_in_lang):
    valid_words = 0
    string_data = str(a_case_data)
    # process data for ()
    #if '(' in string_data:              # case some letters have interference
    if True:
        possible_letters = ""
        list_case_data = []
        parenthesis = False
        for i in range(len(string_data)):              # range length word in this language
            a_char = string_data[i]
            if string_data[i] == '[' or string_data[i] == ']':
                pass
            elif string_data[i] =='/' or string_data[i] == '\'':
                pass
            elif string_data[i] =='//' or string_data[i] == '\\':
                pass
            elif string_data[i] == '(':
                if possible_letters != "":
                        list_case_data.append(possible_letters)
                possible_letters = ""
                parenthesis = True
            elif string_data[i] == ')':
                list_case_data.append(possible_letters)
                possible_letters = ""
                parenthesis = False
            else:                       # normal char
                if parenthesis:
                    possible_letters += string_data[i]
                else:
                    if possible_letters != "":
                        list_case_data.append(possible_letters)
                    possible_letters = ""
                    possible_letters += string_data[i]
        if possible_letters != "":
            list_case_data.append(possible_letters)
        print a_case_data
        assert l == len(list_case_data), "Error processing list inputs"

        # if there are any () in case data, it has been processed into a new list with each set () its own index
        if '(' in string_data:              # case some letters have interference
        # solve here
            found_words = find_words(list_case_data, l)
            for word in found_words:
                if word in words_in_lang:
                    valid_words += 1
        # no () in data
        else:                               # case 1 word, no interference
            s = ""
            for i in list_case_data:
                s += i
            if s in words_in_lang:

                valid_words += 1

    return valid_words


def find_words(list_case_data, l):
    found_words = []
    index = 0
    partial_word = ""
    recur_find_words(index, list_case_data, l, found_words, partial_word)

    return found_words


def recur_find_words(index, list_case_data, l, found_words, partial_word):
    for i in list_case_data[index]:
        #print i
        #`print list_case_data
        if index+1 == l:
            a_word = partial_word+str(i)
            found_words.append(a_word)
        else:
            recur_find_words(index+1, list_case_data, l, found_words, partial_word+str(i))


if __name__ == "__main__":
    #list_case_data = ['ab', 'bc', 'ca']
    #l = 3
    #found_words = find_words(list_case_data, l)
    #print found_words
"""