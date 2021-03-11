# Noel Wafuko
# nww010 # 11308656
# For Instructor Jeff Long

import numpy as np
from tabulate import tabulate
#quiz data
quizResults = [
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 1]
]
#reshape array
reshapeArr=np.array(quizResults).reshape(-1,2)
print(x)


#map excecutable array
data = np.array(x) 
headers = ["0,0","0,1","1,0","1,1"]
#tabulate the data
table = tabulate(data, headers, tablefmt="github")
print(table)
#calculate percentage 
values = set([y for row in reshapeArr for y in row])
print([[(a==x).sum()*100.0/len(a) for x in values] for a in reshapeArr],'percent solved question 1')
print([[(a==x).sum()*100.0/len(a) for x in values] for a in reshapeArr],'percent solved question 2')
print([[(a==x).sum()*100.0/len(a) for x in values] for a in reshapeArr],'percent solved question 7')
