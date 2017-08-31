#!/usr/bin/python3
from bs4 import BeautifulSoup, Comment, NavigableString
soup = BeautifulSoup(open("html"), 'html.parser')

# Identify the start comment
def begin_comment(text):
    return (isinstance(text, Comment) and
            text in "<!-- Task Body -->")

# Identify the end location
def end_mark(element):
    return element.string == "Repo:"
i = 0
readme = "BY NOOP LION"
# Look for start comments
for starting_point in soup.find_all(text=begin_comment): # get starting point
    readme += ('==================={}=====================\n'.format(i))
    i += 1
    for element in starting_point.find_all_next(True): # get everything in between
        if end_mark(element): # if end comment is found, quit
            break
        readme += str(element) + '\n'

file = open("work.md", "w")
file.write(readme)
file.close()
