# ファイルから入力
# テキストを数値に変換してから、合計を求める。

f = open("scoredata.txt","r", encoding="utf-8")
lines = f.readlines()
s = 0
for line in lines:
    p = int(line.strip())
    s += p
    print("点数=", p, "合計=", s)
l = len(lines)
print("人数=",l)
ave = s / l
print("平均値=",ave)    
f.close()
