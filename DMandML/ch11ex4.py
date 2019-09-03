# TF-IDFを計算
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

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

# 単語帳を表示
terms = vectorizer.get_feature_names()
print("単語文書行列（TF-IDF)=")
print("単語\t",end='')
for term in terms:
    print("%6s" % term, end='')
print()

# TF-IDFを計算
tfidfs = vecs.toarray()
# 計算結果を表示
for n, tfidf in enumerate(tfidfs):
    print("文書", n, "\t", end='')
    for t in tfidf:
        print("%8.4f" % t, end='')
    print() 
