# MeCabテスト
import MeCab

tagger = MeCab.Tagger()
text = "MeCabで遊んでみよう！"
# 解析結果を変数に入れる
tokens = tagger.parse(text) 
# 解析結果を表示する
print(tokens)
