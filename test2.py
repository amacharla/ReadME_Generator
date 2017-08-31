#!/usr/bin/python3
from bs4 import BeautifulSoup, Comment, NavigableString
soup = BeautifulSoup(open("htmlstuff.htm"), 'html.parser')

# Identify the end location
def end_mark(element):
    return element.string == "Repo:"

readme = ""
# Look for start comments
for starting_point in soup.find_all(class_="task"): # get starting point
    readme += str(starting_point)
    for element in starting_point.find_next_siblings(True):
        if end_mark(element):
            readme += '\n\n'
            break
        readme += str(element)
file = open("work2.md", "w")
file.write(readme)
file.close()
