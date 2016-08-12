"""
@author: David Lei
@since: 25/07/2016
@modified:

https://www.youtube.com/watch?v=ZdDOauFIDkw

"""

# used for string serching and manipulation i.e. web scraping
import re
print(re.split(r'\s*','here are some words'))
'''
r means evaluate this string differently '\' will mean something different
\s is a space character, after some space character (any number due to *)
then split it up

above will result in ['here', 'are', 'some', 'words']
'''

print(re.split(r'(\s*)','here are some words')) # () group and includes, spaces in list

print(re.split(r'(s*)','here are some words')) # s evaluateed as regular char now, \s means space

print(re.split(r'[a-f]', 'abcdkfjFt')) # split up list a-f is a through f, so split at things a through f

print(re.split(r'[A-F0-9]', 'abcd90112kfjFasdmt',
               re.I|re.M)) # split up list a-f is a through f, so split at things a through f
                # re.I is ignore case, re.M eval multiline

# [] look for a char that satifies this range

print(re.split(r'[a-f][a-f]', 'abbasdboqwbbnklmz'))

'''
/d = loook for digits = [0-9]
/D = look for reverse of ^

* = 0 or more
+ = 1 or more
? = 0 or 1 of..
[5] = exact number..
[1,60] = range on number of..
'''

print(re.findall(r'\d', 'ahsd907.ansiho81'))

print(re.findall(r'\d{1,5}', 'ahsd907.ansiho81'))
# find lists of 1-5 digits
print(re.findall(r'\d{2}', 'ahsd907.ansiho81'))
# find lists of 2 digits
