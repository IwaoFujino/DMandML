# 自己相関係数
# 日経平均株価（終値）+ ニューヨークダウ平均株価（終値） + 円ドルレート（終値）
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSVファイル読み込み
mydf1 = pd.read_csv('NIKKEI20152018.csv', index_col=0, parse_dates=[0])
#print(mydf1.head())
mydf2 = pd.read_csv('NEWYORK20152018.csv', index_col=0, parse_dates=[0])
#print(mydf2.head())
mydf3 = pd.read_csv('USDJPY20152018.csv', index_col=0, parse_dates=[0])
#print(mydf3.head())
mydf = pd.merge(mydf1, mydf2, on='日付')
mydf = pd.merge(mydf, mydf3, on='日付')
#print(mydf.head())
mydf = mydf.sort_index()
#print(mydf.head())
N = len(mydf)
print('N=',N)

nikkei = mydf['NIKKEI終値']
nikkei = nikkei.apply(lambda x: x.replace(',','')).astype(np.float)
newyork = mydf['NEWYORK終値']
newyork = newyork.apply(lambda x: x.replace(',','')).astype(np.float)
usdjpy = mydf['USDJPY終値']

L = 20
tao = np.empty(2*L+1)
corrcoef1 = np.empty(2*L+1)
corrcoef2 = np.empty(2*L+1)
corrcoef3 = np.empty(2*L+1)
for t in range(2*L+1):
    tt = t-L
    tao[t] = tt
    nikkei_shift = nikkei.shift(tt)
    newyork_shift = newyork.shift(tt)
    usdjpy_shift = usdjpy.shift(tt)
    if tt>0:
        corrcoef1[t] = np.corrcoef(nikkei[tt:N], nikkei_shift[tt:N])[0,1]
        corrcoef2[t] = np.corrcoef(nikkei[tt:N], newyork_shift[tt:N])[0,1]
        corrcoef3[t] = np.corrcoef(nikkei[tt:N], usdjpy_shift[tt:N])[0,1]
    else:
        corrcoef1[t] = np.corrcoef(nikkei[0:N+tt], nikkei_shift[0:N+tt])[0,1]
        corrcoef2[t] = np.corrcoef(nikkei[0:N+tt], newyork_shift[0:N+tt])[0,1]
        corrcoef3[t] = np.corrcoef(nikkei[0:N+tt], usdjpy_shift[0:N+tt])[0,1]
    print("tao=%4d  corr1=%7.4f  corr2=%7.4f  corr3=%7.4f" % (tao[t], corrcoef1[t], corrcoef2[t], corrcoef3[t]))

# グラフ表示
# figure1
plt.figure(num=1, figsize=(8, 5), dpi=180, facecolor='w', edgecolor='k')
plt.title('Correlation Coefficient of NIKKEI (price)')
plt.xlabel('tao')
plt.ylabel('corrcoef')
plt.grid()
plt.plot(tao, corrcoef1, color='blue')
plt.show()
# figure2
plt.figure(num=2, figsize=(8, 5), dpi=180, facecolor='w', edgecolor='k')
plt.title('Correlation Coefficient between NIKKEI and NEWYORK (price)')
plt.xlabel('tao')
plt.ylabel('corrcoef')
plt.grid()
plt.plot(tao, corrcoef2, color='blue')
plt.show()
# figure3
plt.figure(num=3, figsize=(8, 5), dpi=180, facecolor='w', edgecolor='k')
plt.title('Correlation Coefficient between NIKKEI and USDJPY (price)')
plt.xlabel('tao')
plt.ylabel('corrcoef')
plt.grid()
plt.plot(tao, corrcoef3, color='blue')
plt.show()