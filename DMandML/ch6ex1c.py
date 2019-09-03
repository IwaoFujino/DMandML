# k-平均法アルゴリズムの理解
import numpy as np

data=[
[1, 2],
[3, 1],
[2, 3],
[3, 6],
[4, 6],
[7, 2],
[7, 4],
]
#  クラスタ数
K=3
pdata=np.array(data)
N, L=np.shape(pdata)
cdata=np.empty([K,L])
#　クラスタ中心を計算
cdata[0]=[(pdata[0,0]+pdata[1,0]+pdata[2,0])/3.0, (pdata[0,1]+pdata[1,1]+pdata[2,1])/3.0] 
cdata[1]=[(pdata[5,0]+pdata[6,0])/2.0, (pdata[5,1]+pdata[6,1])/2.0] 
cdata[2]=[(pdata[3,0]+pdata[4,0])/2.0, (pdata[3,1]+pdata[4,1])/2.0] 
# クラスタの中心点
print("クラスタの中心点:")
for k in range(K):
    print(cdata[k])
# 各クラスタの中心から各データまでの距離を計算
print("クラスタの中心から各データまでの距離:")
for k in range(K):
    for n in range(N):
        distance=np.sqrt(np.square(cdata[k,0]-pdata[n,0])+np.square(cdata[k,1]-pdata[n,1]))
        print("%8.4f" % distance, end="")
    print()
