import numpy as np
v=np.array([[2],[3]])#Column vector
w=np.array([[5],[7]])#Column vector

print("matrix addition:",v+w)
print("matrix multiplication:",np.matmul(v,w.T))
print("dot product:",np.dot(v.T,w))
print("matrix with multiple operations:",3*v-w)

print("Finding the output vetor:")

result= v+w
print(result)

print("Scaler:")# scaler are numbers that strech or squeeze the vector.

matrix= np.array([[1,2],
                      [3,4]])# here the first column will be i vector and second will be j vector
scaler=np.array([2,3])

output=matrix*scaler #now the i vector will scales by 2 and j vector by 3
print(output)

print("transformation matrix:")
##Transformation of any vector mean , it stretchs the X-direction by 2 times and Y-direction by 3 times.

print("find T([4,5])")
a=np.array([4,5])
scaler1=np.array([2,3])
result=a*scaler1
print(result)

print("rotation matrix:")
matrix1= np.array([[0,-1],
                      [1,0]]) #This is rotation matrix
x=np.array([1,2])
print(np.matmul(matrix1,x))

print("finding determinant of a matrix:")
matrix2= np.array([[1,2],[3,4]])
det=np.linalg.det(matrix2)#linalg use to find determinant.
print(det)

print("Identity matrix:")
indent_matrix=np.eye(3)#np.eye is used to make identity matrix by giving the dimension of matrix.
print(indent_matrix)

g_matrix=np.array([[1,9,7],
                   [8,2,5],
                   [5,7,4]])

print("Rank of matrix:")
print(np.linalg.matrix_rank(g_matrix))#Rank of matrix, it can define the dimensions of matrix.


# eigen vectors: vectors that remains same of direction after scaling or squeeze them.
# eigen value : it is number by which vectors are scaled.

print("finding eigenvalues:")

print("finding eigenvectors:")
results,x=np.linalg.eig(g_matrix)
print(x)#it will give eigen vectors
print(results)#will print eigen values, for getting only eigen values use  .eigvals



