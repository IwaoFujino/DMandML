# k-平均法アルゴリズム
import numpy as np

#　データ集合
data=[
[1, 2],
[3, 1],
[2, 3],
[3, 6],
[4, 6],
[7, 2],
[7, 4],
]
#　クラスタ中心の初期値
cdata=[
[2, 2],
[4, 4],
[6, 6],
]
# クラスタの数
K=3
pdata=np.array(data, dtype=float)
cdata=np.array(cdata, dtype=float)
N, L=np.shape(pdata)
distance=np.empty([K,N])
for m in range(4):
    print("m=", m)
    # 中心点とデータ点の間の距離を計算
    print("距離:")
    for k in range(K):
        for n in range(N):
            distance[k,n]=np.sqrt(np.square(cdata[k,0]-pdata[n,0])+np.square(cdata[k,1]-pdata[n,1]))
            print("%8.4f" % distance[k,n], end="")
        print()
    # クラスタラベルを求める
    labels=np.argmin(distance, axis=0)
    print("クラスタラベル=",labels)
    label=list(set(labels))
    # クラスタの中心座標を計算
    print("クラスタの中心:")
    for l in label:
        ldata=pdata[labels==l]
        cdata[l,:]=np.average(ldata,axis=0)
    print(cdata)
# 最終結果を表示
print("最終結果：")
print("データ=", data)
print("クラスタラベル=", labels)
