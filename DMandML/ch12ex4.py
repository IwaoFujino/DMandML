# 複数wikiデータファイルから文書の類似度を計算
import MeCab
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import datetime
from os.path import join, relpath
import glob

# 形態素解析器
tagger = MeCab.Tagger()

# 関数定義：wikiデータを読み込む
def readwikidata(path, filenames):
    buf=[]
    docdone=False
    titles=[]
    documents=[]
    doccnt=0
    for filename in filenames:
        wikifile = open(path+"/"+filename,"r", encoding="utf_8")
        #ファイルから1行ずつ処理する
        for line in wikifile:
            if line.startswith('<doc '):
                buf=[]
                docdone=False
                m = re.search('title=.*>' , line)
                title=m.group().replace('title="','')
                title=title.replace('">','').strip()
                print("文書番号=", doccnt, "タイトル=", title)
            elif line.startswith('</doc>'):
                doc=''.join(buf)
                docdone=True
                doccnt+=1
            else:
                if len(line)!=0:
                    buf.append(line)
            words=""
            if docdone==True:
                node = tagger.parseToNode(doc)
                while node:
                    # 形態素属性を分割してリストに入れる
                    node_features=node.feature.split(",")
                    if node_features[0]=="名詞" and (node_features[1]=="一般" or node_features[1]=="固有名詞"):
                        words=words+" "+node_features[6]
                    node = node.next
            if len(words)>=100:
                titles.append(title)
                documents.append(words)

    return(titles, documents)

# 関数定義：TF-IDFを計算
def calculatetfidf(titles, docs):  
    # オブジェクト生成
    npdocs=np.array(docs)
    vectorizer = TfidfVectorizer(norm=None, smooth_idf=False)
    vecs = vectorizer.fit_transform(npdocs)
    # TF-IDF
    tfidfs = vecs.toarray()
    # TF-IDFを計算
    tfidfs = vecs.toarray()

    return tfidfs

# コサイン類似度
def calculatesimilarity(titles, tfidfs):
    similarity = cosine_similarity(tfidfs)
    # 計算結果を表示
    for n1, simi in enumerate(similarity):
        print("-------文書1 = %d   タイトル = %s ----------" % (n1, titles[n1]))
        for n2, s in enumerate(simi):
            if( n1!=n2 and s>=0.2):
                print("文書1=%s 文書2=%s 類似度=%8.6f" % (titles[n1], titles[n2], s))

    return

# メイン処理
def main():
    #ファイル名を指定
    wikipath="./wikidata/wikiarticles/AA"
    #wikipathにある全ファイル名を取得する
    #filenames=[relpath(x, wikipath) for x in glob.glob(join(wikipath, '*'))]
    #ファイル名を指定する
    filenames=['wiki_00', 'wiki_01', 'wiki_02', 'wiki_03']   
    wikifilenames =sorted(filenames)
    wikititles, wikidocuments=readwikidata(wikipath, wikifilenames)
    print("TF-IDFを計算します... ")
    wikitfidfs=calculatetfidf(wikititles, wikidocuments)
    print("類似度を計算します... ")
    calculatesimilarity(wikititles, wikitfidfs)

# ここから実行する
if __name__ == "__main__":
	start_time = datetime.datetime.now()
	main()
	end_time = datetime.datetime.now()
	elapsed_time=end_time-start_time
	print("経過時間=", elapsed_time)
	print("すべて完了 !!!")
