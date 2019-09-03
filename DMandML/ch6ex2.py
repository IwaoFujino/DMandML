# k-平均法
from sklearn import cluster

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
print("データ=",data)
# k-means モデルの作成
# クラスタ数はを3に指定
model = cluster.KMeans(n_clusters=3)
model.fit(data)
# クラスタリング結果ラベルの取得
labels = model.labels_
print("ラベル=", labels)
# 新しいデータを与えて、そのクラスタラベルを求める
newdata=[
[6,3]
]
print("新しいデータ=", newdata)
newlabel=model.predict(newdata)
print("新しいデータのラベル=", newlabel)
