#!/usr/bin/python3
from bs4 import BeautifulSoup, Comment, NavigableString
soup = BeautifulSoup(open("htmlstuff.htm"), 'html.parser')

# Identify the start comment
def begin_comment(text):
    return (isinstance(text, Comment) and
            text in "<!-- Progress vs Score -->")

# Identify the end comment
def end_comment(text):
    return (isinstance(text, Comment) and
            text in "<!-- Task URLs -->")

# Look for start comments
for starting_point in soup.find_all(text=begin_comment): # get starting point
    for text in starting_point.find_all_next(text=True): # get everything in between
        if end_comment(text): # if end comment is found, quit
            break
        print (text)
