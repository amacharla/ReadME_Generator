#!/usr/bin/python3
from bs4 import BeautifulSoup, Comment, NavigableString
from sys import argv

if len(argv) != 2:
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
        readme += str(element.encode(encoding="ascii", errors="xmlcharrefreplace"))

print(readme)
# Writing to ReadMe File
file = open("README.md", 'w')
file.write(readme)
file.close()
