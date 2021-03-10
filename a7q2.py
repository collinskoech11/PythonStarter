import numpy as np


f = open("provincial_seats.txt", "r")
lines = f.readlines()

my_list = f
my_array = np.array(my_list)

print (str(my_array))

res = (len([ele for ele in my_array if ele > 0]) / len(my_array)) * 100

print(str(res))