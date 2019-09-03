#　階層型クラスタリング、結果を整理
import scipy.cluster.hierarchy as hclst

data = [[1,2], [3,1],[2,3],[3,6],[4,6],[7,2],[7,4]]

print("Data:")
for no, d in enumerate(data):
    print("no=",no, "data=", d)

# クラスタリングは以下の 1 行だけ。
results = hclst.linkage(data,method='single',metric='euclidean')
#results = hclst.linkage(data,method='complete',metric='euclidean')
#results = hclst.linkage(data,method='ward',metric='euclidean')

# 結果の表示
print("Results:")
for res in results:
    print(res)

# 結果の整理と表示
cluster_tree=[x for x in range(len(data))]
clusters=[x for x in range(len(data))]
n=0
distance_max=6
print("Clusters:")
for a, b, distance, represent in results:
    if distance <= distance_max:
        print("a=",int(a), "b=",int(b), distance, represent)
        if(int(a)>=len(data)):
            c=cluster_tree[int(a)]
        else:
            c=int(a)
        if(int(b)>=len(data)):
            d=cluster_tree[int(b)] 
        else: 
            d=int(b)
        cluster_tree.append((c, d))
        clusters.remove(c)
        clusters.remove(d)
        clusters.append((c, d))
        print(">>>> n=",n,  "number of clusters=", len(clusters), "clusters=", clusters)
        n+=1
