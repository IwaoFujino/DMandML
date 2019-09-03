# 時系列数値データの自己相関係数とグラフ表示
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSVファイル読み込み
mydf = pd.read_csv('TokyoTemp20082017.csv', index_col=0, parse_dates=[0], dtype='float')
tokyo = mydf['Temp(C)']
print(tokyo.head())
N = len(tokyo)
print("N=", N)

# 自己相関係数を算出
L = 365*2
m = np.empty(2*L+1)
corrcoef = np.empty(2*L+1)
for t in range(2*L+1):
    tt = t-L
    m[t] = tt
    tokyo_shift = tokyo.shift(tt)
    if tt>0:
        corrcoef[t] = np.corrcoef(tokyo[tt:N], tokyo_shift[tt:N])[0,1]
    else:
        corrcoef[t] = np.corrcoef(tokyo[0:N+tt], tokyo_shift[0:N+tt])[0,1]
    print("m=", m[t], "corrcoef=", corrcoef[tt])

# グラフ表示
plt.figure(num=None, figsize=(8, 5), dpi=180, facecolor='w', edgecolor='k')
plt.title('Correlation Coefficient of Tokyo Temperature')
plt.xlabel('m')
plt.ylabel('corrcoef')
plt.grid()
plt.plot(m, corrcoef, color='blue')
plt.show()
