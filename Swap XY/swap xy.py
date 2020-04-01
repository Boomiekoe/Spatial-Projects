print "Memulai Tool"
import csv
import sys
import os

script_folder = sys.path[0]
tools_folder = os.path.dirname(script_folder)

with open('CoorList.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        lsIn = []
        for el in row:
            sub = el.split(', ')
            lsIn.append(sub)
        z = []
        c = 0
        d = len(lsIn)
        for el in lsIn:
            if c < d:
                x = []
                y =[]
                x = lsIn[c+1]
                y = lsIn[c]
                x.extend(y)
                z.append(x)
                c = c+2
            else:
                pass
        print z
    
    
