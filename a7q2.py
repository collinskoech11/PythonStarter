import numpy as np


f = open("provincial_seats.txt", "r")
lines = f.readlines()

my_list = f
my_array = np.array(my_list)

print (str(my_array))

x=np.array(my_array).reshape(-1,3)

ptint(x)