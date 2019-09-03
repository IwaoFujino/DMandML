# 散布図を描く
import numpy as np
from matplotlib import pyplot as plt

data=[
[1, 2],
[3, 1],
[2, 3],
[3, 6],
[4, 6],
[7, 2],
[7, 4],
]

pdata=np.array(data)
plt.title("Scatter Graph of Data")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.scatter(pdata[:,0], pdata[:,1])
plt.show()