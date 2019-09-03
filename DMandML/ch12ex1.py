# wikiデータを読み込む
import MeCab
import re

#ファイルから読む
filename="./wikidata/wikiarticles/AA/wiki_00"
wikifile = open(filename,"r", encoding="utf_8")
tagger = MeCab.Tagger()
buf=[]
docdone=False
titles=[]
documents=[]
doccnt=0
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
    # 各タイトルの単語を取り出す
    words=""
    if docdone==True:
        node = tagger.parseToNode(doc)
        while node:
            #print(node.surface + '\t' + node.feature)
            # 形態素属性を分割してリストに入れる
            node_features=node.feature.split(",")
            if node_features[0]=="名詞" and (node_features[1]=="一般" or node_features[1]=="固有名詞"):
                 words=words+" "+node.surface
            node = node.next
    if(len(words)>=100):
        titles.append(title)
        documents.append(words)
# タイトルと単語を表示。文書数を表示
for title, words in zip(titles, documents):
    print(title, ">>>")
    print( words)
print("文書数=", len(documents))
