#　ファイルへ出力
# 数値を文字列に変換してから、ファイルへ書き出す

f = open("newdata.txt","w", encoding="utf-8")
pp = [45, 67, 38, 87, 56, 78, 91, 45, 64, 86, 90, 45]
for p in pp:
    print("点数=", p)
    f.write(str(p) + "\n") 
f.close()
