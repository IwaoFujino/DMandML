# クラスタの中心と要素の間の距離を求める
import numpy as np

# データの要素
data = [
[1.0, 2.0],
[3.0, 1.0],
[2.0, 3.0],
[3.0, 6.0],
[4.0, 6.0],
[7.0, 2.0],
[7.0, 4.0],
]
# クラスタ中心の初期値
cdata = [
[2.0, 2.0],
[4.0, 4.0],
[6.0, 6.0],
]
# クラスタの数
K = 3
pdata = np.array(data)
cdata = np.array(cdata)
N, L = np.shape(pdata)
# 中心点
print("中心点:")
for k in range(K):
    print(cdata[k])
# 中心点とデータ点の間の距離
print("中心点とデータ点の間の距離:")
for k in range(K):
    for n in range(N):
        distance = np.sqrt(np.square(cdata[k,0] - pdata[n,0]) + np.square(cdata[k,1]-pdata[n,1]))
        print("%8.4f" % distance, end="")
    print()
