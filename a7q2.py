import numpy as np

#read data from dataset
f = open("provincial_seats.txt", "r")
lines = f.readlines()

#strip data to one line
mylist = [line.rstrip('\n') for line in f]

#convert data into an array
myarray = np.array(mylist)

print(myarray)

#reshape array
reshapeMyArr = np.reshape(myarray, (-1,3))
# newArr = arr.reshape(3, 13)
print(reshapeMyArr)
