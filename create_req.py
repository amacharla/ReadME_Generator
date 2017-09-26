#!/usr/bin/python3
from bs4 import BeautifulSoup, Comment, NavigableString
from sys import argv

if len(argv) != 2:
    print("Need to pass in README.md with HTML SourceCode")
    exit()

# open html file (1st argument) and parse through source code
fd = open(argv[1], 'r')
soup = BeautifulSoup(fd, 'html.parser')

# Identify the end location, stop at <pre>
def end_mark(element):
    return element.name == "pre"

readme = ""
# Look for start comments
for starting_point in soup.find_all(class_="task"): # set starting point
    readme += str(starting_point) # add Task Header
    for element in starting_point.find_next_siblings(True): # get all requirments
        if end_mark(element): # stop at precode
            readme += '\n\n'
            break
        readme += str(element)

print(readme)
# Writing to ReadMe File
fd2 = open("README.md", 'w')
fd2.write(readme)
fd2.close()
fd.close()
