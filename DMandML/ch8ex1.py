# SVM法で分離直線を求める
import numpy as np
from matplotlib import pyplot as plt

#データを用意
xx = np.array([
[1, 2],
[2, 4],
[3, 4],
[2, 1],
[4, 2],
[4, 3],
])
y = np.array([-1, -1, -1, 1, 1, 1])

# 最適方向ベクトルを計算する
nn = 6
coef = np.empty([nn, nn])
for i in range(nn-1):
    for j in range(nn):
        if i==j:
            coef[i,j] = 2*y[i]*y[j]*np.dot(xx[i], xx[j])
        else:
            coef[i,j] = y[i]*y[j]*np.dot(xx[i], xx[j])
for j in range(nn):
    coef[nn-1,j] = y[j]
d = np.array([2, 2, 2, 2, 2, 0])
alpha = np.linalg.solve(coef,d)
for i in range(nn):
    print("alpha"+str(i)+"=", alpha[i])
mm = 2
wstar = np.empty(mm)
for m in range(mm):
    wstar[m] = 0
    for i in range(nn):
        wstar[m] += alpha[i]*y[i]*xx[i,m]
    print("wstar"+str(m)+"=", wstar[m])

# 切片を計算する
xs = np.array([
[1, 2],
[3, 4],
[2, 1],
[4, 3],
])
ys = np.array([-1, -1, 1, 1])
bs = ys-np.dot(wstar,xs.T)
b = bs.mean()
print("b=", b)

# 訓練データと分離直線のグラフを描く
xx1 = xx[y==-1]
xx2 = xx[y==1]
pdata1 = np.array(xx1)
pdata2 = np.array(xx2)
plt.scatter(pdata1[:,0], pdata1[:,1], marker="x", s=60, linewidth="2", label="Negative Class")
plt.scatter(pdata2[:,0], pdata2[:,1], marker="o", s=60, linewidth="2", label="Positive Class")
kk = 6
x1 = np.empty(kk)
x2 = np.empty(kk)
for i in range(kk):
    x1[i] = i
    x2[i] = -(wstar[0]*x1[i]-b)/wstar[1]

plt.title("SVM Result of Training Data")
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid()
plt.plot(x1, x2, marker=".")
plt.legend()
plt.show()