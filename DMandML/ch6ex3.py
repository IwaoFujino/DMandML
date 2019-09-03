# k-平均法 ＋　グラフ表示
import numpy as np
from sklearn import cluster
import matplotlib.pyplot as plt

# データを作成
data=[
[1, 2],
[3, 1],
[2, 3],
[3, 6],
[4, 6],
[7, 2],
[7, 4],
]
data=np.array(data)

# k-means モデルの作成
# クラスタ数は 3 を指定
model = cluster.KMeans(n_clusters=3)
model.fit(data)
# クラスタリング結果ラベルの取得
labels = model.labels_

# 結果をグラフにする
plt.figure(1)
# ラベル 0 の描画
ldata = data[labels == 0]
plt.scatter(ldata[:, 0], ldata[:, 1], marker='s', color='green')
# ラベル 1 の描画
ldata = data[labels == 1]
plt.scatter(ldata[:, 0], ldata[:, 1], marker='o', color='red')
# ラベル 2 の描画
ldata = data[labels == 2]
plt.scatter(ldata[:, 0], ldata[:, 1], marker='^', color='blue')
#　タイトルとx軸、y軸ラベルの設定
plt.title("Scatter Plot of Clustered Data")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
