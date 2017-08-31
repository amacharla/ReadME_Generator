#!/usr/bin/python3

from bs4 import BeautifulSoup, Comment, NavigableString

with open("htmlstuff.htm") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    tasks = soup.find_all("h4", class_="task")
    header = []
    for t in tasks:
        head = str(t.contents[0])
        header.append("".join(head))
        req = str(t.find_next().contents[0])
        header.append(req.strip(' \n'))
    # print("".join(header))

    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    for c in comments:
        if c in "<!-- Task Body -->":
                print(c.next_sibling.next)
            #while c.next_sibling not in "<!-- Task URLs -->":
                  #  print()
        #print(comment)
    #taskname = "".join([i.contents[0] for i in tasks])
    #print(taskname)
    #requirments = "".join([i.find_next().contents[0] for i in tasks])
    #print(requirments)

    #file = open("work.md", "w")
    #file.write(taskname)
    #file.close()

