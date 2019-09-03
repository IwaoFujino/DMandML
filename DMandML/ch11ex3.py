# MeCab:固有名詞、一般名詞を抽出
import MeCab

tagger = MeCab.Tagger()
text = '日本国民は、正当に選挙された国会における代表者を通じて行動し、\
われらとわれらの子孫のために、諸国民との協和による成果と、\
わが国全土にわたって自由のもたらす恵沢を確保し、\
政府の行為によって再び戦争の惨禍が起ることのないようにすることを決意し、\
ここに主権が国民に存することを宣言し、この憲法を確定する。'
print("日本語の文：")
print(text)

doc=[]
node = tagger.parseToNode(text)
while node:
    # print(node.surface + '\t' + node.feature)
	# 形態素属性を分割してリストに入れる
    node_features=node.feature.split(",")
    if node_features[0]=="名詞" and (node_features[1]=="一般" or node_features[1]=="固有名詞"):
        doc.append(node.surface)
    node = node.next

print('名詞リスト：')
for word in doc:
    print(word)
