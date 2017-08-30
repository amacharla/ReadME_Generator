#!/usr/bin/python3

from bs4 import BeautifulSoup

with open("everythingObject.htm") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    tasks = soup.find_all("h4", class_="task")
    taskname = "".join([i.contents[0] for i in tasks])
    print(taskname)
    file = open("work.md", "w")
    file.write(taskname)
    file.close()

