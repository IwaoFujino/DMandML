# wikiデータのTFIDFを計算する
import MeCab
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

tagger = MeCab.Tagger()

# 関数定義：wikiデータを読み込む
def read_wikidata(filename):
    wikifile = open(filename,"r", encoding="utf_8")
    tagger = MeCab.Tagger('-Ochasen')
    buf=[]
    docdone=False
    titles=[]
    documents=[]
    doccnt=0
    #ファイル読んでから1行ずつ処理する
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
                    words=words+" "+node.surface
                node = node.next

        if len(words)>=100:
            titles.append(title)
            documents.append(words)

    return(titles, documents)

# 関数定義：TFIDFを計算
def calculate_tfidf(titles, docs):  
    # オブジェクト生成
    npdocs=np.array(docs)
    vectorizer = TfidfVectorizer(norm=None, smooth_idf=False)
    vecs = vectorizer.fit_transform(npdocs)
    # 単語帳を表示
    terms = vectorizer.get_feature_names()
    print("単語文書行列（TF-IDF)=")
    print("単語","\t",end='')
    for term in terms:
        print("%6s  " % term, end='')
    print()
    # TF-IDFを計算
    tfidfs = vecs.toarray()
    # 計算結果を表示
    for n, tfidf in enumerate(tfidfs):
        print("文書番号=", n, "タイトル=", titles[n], ">>>", end='')
        for t in tfidf:
            if(t!=0.0000):
                print("%10.4f" % t, end='')
        print() 

    return tfidfs

# メイン処理
wikifilename="./wikidata/wikiarticles/AA/wiki_00"
wikititles, wikidocuments=read_wikidata(wikifilename)
wikitfidfs=calculate_tfidf(wikititles, wikidocuments)
