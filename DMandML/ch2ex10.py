# 繰り返しfor文＋リスト
# 平均値を求める

pp=[45, 67, 38, 87, 56, 78, 91, 45, 64, 86, 90, 45]
s = 0
for p in pp:
    s += p
    print("点数=", p, "合計=", s)
l = len(pp)
print("人数=",l)
ave = s / l
print("平均値=",ave)
