# MeCab　品詞情報分離
import MeCab

tagger = MeCab.Tagger()
text = "MeCabで遊んでみよう！"
# 解析結果を変数に入れる
node = tagger.parseToNode(text) 
# node.surface 形態素の表記
# node.feature 形態素の品詞、読みなど属性情報
while node:
    print(node.surface + '\t',end='')
    node_features = node.feature.split(",")
    for nf in node_features:
        print(nf + '/',end='')
    print()
    node = node.next
