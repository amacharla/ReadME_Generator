#!/usr/bin/python3
# ReadMEGenerator Version 1
# Created by Anoop Macharla 08-15-17

from bs4 import BeautifulSoup, Comment, NavigableString
from sys import argv

# Arguments check
if len(argv) != 2:
    print("Need to pass in a file with HTML SourceCode")
    exit()

# open html file (1st argument) and parse through source code
fd = open(argv[1], 'r')
soup = BeautifulSoup(fd, 'html.parser')

# Identify the end location, stop at <pre> or before Repository info
def end_mark(element):
        return element.name == "pre" or element.string == "Repo:"

#Start conversion process
readme = ""
problems = 0
title = soup.find(class_="gap")
readme += str(title) + '\n\n' # add Assignment Title

# Find Each Task and Parse through content
for starting_point in soup.find_all(class_="task"): # Task found
    readme += '\n' + str(starting_point) # add Task Header
    problems += 1
    for element in starting_point.find_next_siblings(True): # get all requirments
        if element(class_="task_progress_score_text"): # dont include Score Bar
            continue
        if element.name == "iframe":
            readme += str(element.get('src'))
            continue
        if end_mark(element): # stop at precode or repo info
            readme += '\n\n'
            break
        readme += str(element)

# Create and Write  ReadMe File
fd2 = open("README.md", 'w')
fd2.write(readme)
fd2.close()
fd.close()

print("=============== Summary ====================")
print("Assignment: {:s}".format(str(title.contents)[2:-2]))
print("Number of Tasks: {:d}".format(problems))
print("===== README.md Successfully Generated =====")
