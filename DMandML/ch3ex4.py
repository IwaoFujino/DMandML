# numpyの使い方
import numpy as np

a=np.array([[0,1], [2,3], [4,5]])
print("行列a=")
print(a)
print("次元:", a.ndim)
print("行数、列数:", a.shape)
b=np.array([[6,5], [4,3], [2,1]])
print("行列b=")
print(b)
print("次元:", b.ndim)
print("行数、列数:", b.shape)
c = a.T.dot(b)
print("行列c=")
print(c)
print("次元:", c.ndim)
print("行数、列数:", c.shape)
