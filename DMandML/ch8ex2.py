# データ集合の座標変換、変換前と変換後の散布図
import numpy as np
from matplotlib import pyplot as plt

# データを生成
nn = 17
r1 = 10
r2 = 20
sita = np.linspace(0, 360, nn) / 180.0*np.pi
xx1 = np.empty([nn,2])
xx2 = np.empty([nn,2])
xx1[:,0] = r1*np.cos(sita)
xx1[:,1] = r1*np.sin(sita)
xx2[:,0] = r2*np.cos(sita)
xx2[:,1] = r2*np.sin(sita)

# 散布図を描く
plt.figure(1)
plt.title("Scatter Graph of Original Data")
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid()
plt.scatter(xx1[:,0], xx1[:,1], marker="x", s=60, linewidth="2", label="Negative Class")
plt.scatter(xx2[:,0], xx2[:,1], marker="o", s=60, linewidth="2", label="Positive Class")
plt.legend()
plt.show()

# データを変換
s = 1.0e-3
yy1 = np.empty(np.shape(xx1))
yy2 = np.empty(np.shape(xx2))
yy1[:,0] = np.exp(-s*(xx1[:,0]*xx1[:,0] + xx1[:,1]*xx1[:,1]))
yy1[:,1] = np.arctan(xx1[:,1] / xx1[:,0])/np.pi
yy2[:,0] = np.exp(-s*(xx2[:,0]*xx2[:,0] + xx2[:,1]*xx2[:,1]))
yy2[:,1] = np.arctan(xx2[:,1] / xx2[:,0])/np.pi

# 散布図を描く
plt.figure(2)
plt.title("Scatter Graph of Transformed Data")
plt.xlabel("y1")
plt.ylabel("y2")
plt.grid()
plt.scatter(yy1[:,0], yy1[:,1], marker="x", s=60, linewidth="2", label="Negative Class")
plt.scatter(yy2[:,0], yy2[:,1], marker="o", s=60, linewidth="2", label="Positive Class")
plt.legend()
plt.show()
