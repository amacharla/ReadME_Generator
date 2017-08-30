#!/usr/bin/python3

from bs4 import BeautifulSoup

with open("everythingObject.htm") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    print(soup.pre)
    file = open("workfile.md", "w")
    file.write(str(soup.pre))
    file.close()

