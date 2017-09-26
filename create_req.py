#!/usr/bin/python3
from bs4 import BeautifulSoup, Comment, NavigableString
from sys import argv

if len(argv) != 2 and argv[1] != "README.md":
    print("Need to pass in README.md with HTML SourceCode")
    exit()

# open html file (1st argument) and parse through source code
print("===== Reading Source Code =====")
fd = open(argv[1], 'r')
soup = BeautifulSoup(fd, 'html.parser')

# Identify the end location, stop at <pre>
def end_mark(element):
    return element.name == "pre"

#Start conversion process
print("===== Started Conversion Process =====")
readme = ""
problems = 0
title = soup.find(class_="gap")
readme += str(title)

# Look for start comments
print("----- Parsing through {:s} -----".format(str(title.contents)))
for starting_point in soup.find_all(class_="task"): # set starting point
    readme += str(starting_point) # add Task Header
    problems += 1
    for element in starting_point.find_next_siblings(True): # get all requirments
        if end_mark(element): # stop at precode
            readme += '\n\n'
            break
        readme += str(element)

print("----- Made README for {:d} problems -----".format(problems))
print("===== Conversion Process Successful!! =====")
# Writing to ReadMe File
fd2 = open("README.md", 'w')
fd2.write(readme) # overwriting README.md file
fd2.close()
fd.close()
print("===== Readme Successfully Generated =====")
