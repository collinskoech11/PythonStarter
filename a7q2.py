import numpy as np

f = open("provincial_seats.txt", "r")
lines = f.readlines()
mylist = [line.rstrip('\n') for line in f]

myarray = np.array(mylist)

print(myarray)

reshapeMyArr = np.reshape(myarray, (-1,3))
# newArr = arr.reshape(3, 13)
print(reshapeMyArr)
