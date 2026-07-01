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

_2D_matrix= np.array([[1,2],
                      [3,4]])# here the first column will be i vector and second will be j vector
scaler=np.array([2,3])

output=_2D_matrix*scaler #now the i vector will scales by 2 and j vector by 3
print(output)

print("transformation matrix:")

print("rotation matrix:")
_3D_matrix= np.array([[0,-1],
                      [1,0]])
x=np.array([1,2])
print(np.matmul(_3D_matrix,x))

print("")

