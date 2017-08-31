#!/usr/bin/python3
from bs4 import BeautifulSoup, Comment, NavigableString

# open html file and parse through source code
soup = BeautifulSoup(open("htmlstuff.htm"), 'html.parser')

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
file = open("work2.md", "w")
file.write(readme)
file.close()
