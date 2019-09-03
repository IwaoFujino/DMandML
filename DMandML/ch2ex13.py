#　ファイルから入力
# まとめて読んでから１行ずつ表示する

f = open("textfile.txt","r", encoding="utf-8")
lines = f.readlines()
print("まとめて表示する")
print(lines)
print("１行ずつ表示する")
for line in lines:
    line = line.strip()
    print(line)
f.close()
