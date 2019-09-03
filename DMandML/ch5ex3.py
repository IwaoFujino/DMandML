# 階層型クラスタリング
import scipy.cluster.hierarchy as hclst
from matplotlib import pyplot as plt 

data = [[1,2], [3,1],[2,3],[3,6],[4,6],[7,2],[7,4]]

for no, d in enumerate(data):
    print("no=",no, "data=", d)

# クラスタリングは以下の 1 行だけ。
#results = hclst.linkage(data,method='single',metric='euclidean')
#results = hclst.linkage(data,method='complete',metric='euclidean')
results = hclst.linkage(data,method='ward',metric='euclidean')

# デンドログラムで結果を表示
hclst.dendrogram(results)
plt.title("Dendrogram of Clustering")
plt.xlabel("data number")
plt.ylabel("distance")
plt.show()
