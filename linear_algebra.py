import numpy as np
v=np.array([[2],[3]])
w=np.array([[5],[7]])

print("matrix addition:",v+w)
print("matrix multiplication:",np.matmul(v,w.T))
print("dot product:",np.dot(v.T,w))
print("a answer of a question:",3*v-w)

