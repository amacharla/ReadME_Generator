#!/usr/bin/python3
from bs4 import BeautifulSoup, Comment, NavigableString
from sys import argv

if len(argv) != 2 or argv[1] not in "README.md":
    print("Need to pass in README.md with HTML SourceCode")
    exit()

# open html file and parse through source code
soup = BeautifulSoup(open(argv[1]), 'html.parser')

# Identify the end location
def end_mark(element):
    return element.string == "Repo:"

readme = ""
# Look for start comments
for starting_point in soup.find_all(class_="task"): # set starting point
    readme += str(starting_point) # add Task Header
    for element in starting_point.find_next_siblings(True): # get all requirments and code
        if end_mark(element): # stop before Repo info
            readme += '\n\n'
            break
        readme += str(element)

# Writing to ReadMe File
file = open("README1.md", "w")
file.write(readme)
file.close()
