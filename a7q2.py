import numpy as np

#read data from dataset
datafife = open("provincial_seats.txt", "r")
lines = datafile.readlines()

#strip data to one line
mylistdata = [line.rstrip('\n') for line in datafile]

#convert data into an array
myarray = np.array(mylistdata)

print(myarray)

#reshape array
reshapeMyArr = np.reshape(myarray, (-1,3))
# newArr = arr.reshape(3, 13)
print(reshapeMyArr)

#Calculate the Total Population
test_list = [reshapeMyArr]

res_list = [] 
for i in range(0, len(test_list)) : 
    if test_list[i] == 3 : 
        res_list.append(i) 
res = sum(res_list) 
  
# printing resultant list  
print ("Total Canadian Population : " + str(res))

print('Based on population, the following provinces are over-represented :')


#Calculate Overrepresented and Underrepresentes Provinces
list_data = [reshapeMyArr]
array1 = [int(list_data[i]) for i in range(len(list_data)) if i % 2 == 0]
array2 = [int(list_data[i]) for i in range(len(list_data)) if i % 2 != 0]


#Print Overrepresented and Underrepresentes Provinces
print('Over Represented provinces :' , array1)
print('Over Underrepresented provinces :' , array2)