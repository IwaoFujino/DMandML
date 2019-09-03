# 文書間の類似度
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#　文書集合
docs=[
'国民 安心 安心 安全',
'国民 国民 国民 生活 生活 安心',
'生活 安全 安全',
'生活 生活 生活 安心 安心 安全',
'生活 生活 安心 安心 安心',
] 
print("文書集合=")
for doc in docs:
    print(doc)

# オブジェクト生成
npdocs=np.array(docs)
vectorizer = TfidfVectorizer(norm=None, smooth_idf=False)
vecs = vectorizer.fit_transform(npdocs)
# TF-IDF
tfidfs = vecs.toarray()
# コサイン類似度
similarity = cosine_similarity(tfidfs)

# 計算結果を表示
docno=["文書0", "文書1", "文書2", "文書3", "文書4"]
print("文書No", end='')
for n in docno:
    print("%6s  " % n, end='')
print()
for n, simi in zip(docno, similarity):
    print("%s" % n, end='')
    for s in simi:
        print("%10.4f" % s, end='')
    print()
    