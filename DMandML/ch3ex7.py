# scikit-learnの使い方、回帰問題
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# モデルを設定
clf = linear_model.LinearRegression()
# 日経平均株価データ 
nikkei = [21857.43,
22199.00,
22298.08,
22356.08,
22204.22,
22192.04,
22270.38,
22507.32,
22662.74,
22644.31,
22598.39,
22512.53,
22746.70,
22525.18]
L = len(nikkei)

# 説明変数に取引日の番号を利用
xx = np.arange(1, L+1)
xx = xx.reshape(L, 1)
print("xx=", xx)
# 目的変数に日経平均株価を利用
yy = np.array(nikkei)
yy = yy.reshape(L, 1)
print("yy=", yy)
# 予測モデルを作成
clf.fit(xx, yy)
# 回帰係数
print("回帰係数=", clf.coef_)
# 切片
print("切片=", clf.intercept_)
# 決定係数
print("決定係数=", clf.score(xx, yy))

# グラフ作成
plt.title("Average price of Nikkei stock market")
plt.xlabel("Date Number")
plt.ylabel("Price(Yen)")
plt.grid(True)
# 散布図
plt.scatter(xx, yy)
# 回帰直線
plt.plot(xx, clf.predict(xx))
plt.show()