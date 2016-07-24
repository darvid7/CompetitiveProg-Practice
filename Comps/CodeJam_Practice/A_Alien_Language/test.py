import re
fp = file("A-small-practice.in")
(l, d, n) = [int(x) for x in fp.next().split()]

words_in_lang = [fp.next() for x in range(d)]
print "words in lang : " + str(words_in_lang)
for i in range(1,n+1):
    search_string = fp.next().replace("(", "[").replace(")", "]")
    print "\nsearch_string : " + str(search_string)
    
    search_it = re.compile(search_string).search
    print "search_it : " + str(search_it)
    
    results = filter(search_it, words_in_lang)
    
    found = len(results)
    
    print "results : " + str(results)

    print "\n"
fp.close()

print " -- new stuff --"
l = ["combee", "miltank", "charmander", "bulbasaur"]
find  = "mander"
print re.search(find, "anderson")
print " ---- "
st = re.compile(find).search
print st
b = filter(st, l)
print b

print re.search(find, "combee")
print re.search(find, "charmander")
print re.search(find, "bulbasaur")
print re.search(find, "miltank")
print " >.<"
print re.compile(find).search("charmander")
print "<.>"
print st("charmander")
print st("tanky")
print re.match(find, "charmander")

test = [item for item in l if st(item)]
# found match at charmander, so item (charmander) is an answer
print test
#print st.match(find)
#print st.search(find)
# https://docs.python.org/2/library/re.html#checking-for-a-pair