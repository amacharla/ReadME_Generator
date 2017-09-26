#!/usr/bin/python3
from bs4 import BeautifulSoup, Comment, NavigableString
from sys import argv

if len(argv) != 2 and argv[1] != "README.md":
    print("Need to pass in README.md with HTML SourceCode")
    exit()

# open html file and parse through source code
fd = open(argv[1], 'r')
soup = BeautifulSoup(fd, 'html.parser')

# Identify the end location
def end_mark(element):
    return element.string == "Repo:"

def make_mine(header):
    header.contents[1].insert(0, '-') # adds - mandatory
    #print(header.find_next('p').contents.string) # Write -> Wrote
    return(header)
readme = ""
# Look for start comments
for starting_point in soup.find_all(class_="task"): # set starting point
    readme += str(starting_point) # add Task Header
    for element in starting_point.find_next_siblings(True): # get all requirments and code
        if end_mark(element): # stop before Repo info
            readme += '\n\n'
            break
        if element.name == "pre":
            print(element.prettify(formatter="xml"))
            #readme += str(element.encode(formatter=None))
        #else:
        #    readme += str(element) #FIX THIS
        # Conclusion. the &quot is not retained and there are no attributes in native Beauitful soup to modify this behavior. However something called @damit that can help or try a find and replace function.

#print(readme)
# Writing to ReadMe File
#file = open("README.md", 'w')
#file.write(readme)
#file.close()
