import numpy as np

print("numpy array:::::")
n1 = np.array([[1, 2, 3], [4, 5, 6]])
print(n1)
#type(array_name) for type of array

print("\nnumpy array with only zeros::::")
n2 = np.zeros((6, 2))  #(rows,coloumn) for zero matrix
print(n2)

print("\nnumpy array with same values::::")
n3 = np.full((3, 4), 30)  #first is the dimensions and then value
print(n3)

print("\nnumpy array with values in series::::")
n4 = np.arange(10, 20)  #20 is excluded, use for making array from one number to other number
print(n4)

print("\nnumpy array with skipping some values::::")
n5 = np.arange(2, 100, 10)  #add 10 in 2, 2 and 100 is the range
print(n5)

print("\nnumpy array with random values in a range ::::")
n6 = np.random.randint(2, 100,
                       5)  #2 and 100 is range and 5 is how much random numbers we want, numbers will change everytime we run the code
print(n6)

print("\n checking shape of array::::")
n7 = np.array([[1, 2, 3], [4, 5, 6]])
print(n7.shape)  # shape of the array
print("\narray ::::")
print(n7)
print("\nchanging the shape of array::::")
n7.shape = (3, 2)
print(n7)
print("\nshape now::::")
print(n7.shape)

hyp = np.array([1, 2, 3])
hypr = np.array([4, 5, 6])
print("\nvertical stack::::")
nv3 = np.vstack((hyp, hypr))  #this will join the array's verticaly
print(nv3)

print("\nhorizontal stack::::")
nh3 = np.hstack((hyp, hypr))  #it will join stack horizontally
print(nh3)

print("\ncolumn stack::::")
nc = np.column_stack((hyp, hypr))  #column vise join the array's
print(nc)

print("\nintersection::::")
hy = np.array([[1, 2, 3], [3, 5, 6]])
d = np.array([[1, 2, 9], [8, 6, 9]])
j = np.intersect1d(hy, d)  #intersection of hy and d, substract hy-d
print(j)

print("\nset difference::::")
k = np.setdiff1d(hy, d)  #find the diffrence between arrays
print(k)

print("\naddition::::")
l = np.sum([hy, d])  #normally add the all number
print(l)

print("\nadditon::::")
l1 = np.sum([hy, d], axis=0)  #it will add numbers column-wise,axis =1 willbe sum row wise
print(l1)

print("\n basic arithmatic operations::::")

print("\n basic addition::::")
l = np.array([1, 2, 3])
l1 = l + 1
print(l1)

print("\n basic multiplication::::")
k1 = l * 2
print(k1)

print("\n basic division::::")
j1 = l / 2
print(j1)

print("\n basic subtraction::::")
k2 = l - 2
print(k2)

print("basic math functions::::")

print("\n mean::::")
a = np.array([1, 2, 3, 88, 90])
print(np.mean(a))

print("\n median::::")
print(np.median(a))

print("\n standard deviation::::")
print(np.std(a))

print("\n saving a numpy array::::")
y = np.array([[1, 2, 3], [4, 5, 6]])
np.save('hello',y)# in '' we will right the name in which we want to store the data and y is our array

print("\n loading numpy array::::")
y1 = np.load('hello.npy')# .npy is the extension in which array is stored
print(y1)
