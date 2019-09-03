# 要素番号を使って、リストの要素を表示
# 繰り返しfor文＋リスト

pp=[45, 67, 38, 87, 56, 78, 91, 45, 64, 86, 90, 73]

print("全要素をまとめて表示：")
print("pp=",pp)
print("要素を個別に表示：")
print("最初の要素 点数=",pp[0])
print("2番目の要素 点数=",pp[2])
print("最後の要素 点数=",pp[-1])
print("全要素の数=",len(pp))
print("for文を使って、全要素を表示：")
for i in range(len(pp)):
    print("点数=",pp[i])
