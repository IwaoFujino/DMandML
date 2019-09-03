# 線形回帰モデルによる時系列データの予測 + 評価指標、グラフ表示
# NIKKEIの終値
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import metrics

# CSVファイル読み込み
mydf1 = pd.read_csv('NIKKEI20152018.csv', index_col=0, parse_dates=[0])
mydf2 = pd.read_csv('NEWYORK20152018.csv', index_col=0, parse_dates=[0])
mydf3 = pd.read_csv('USDJPY20152018.csv', index_col=0, parse_dates=[0])
mydf = pd.merge(mydf1, mydf2, on='日付')
mydf = pd.merge(mydf, mydf3, on='日付')
mydf = mydf.sort_index()
N = len(mydf)
nikkei = mydf['NIKKEI終値']
nikkei = nikkei.apply(lambda x: x.replace(',','')).astype(np.float)
newyork = mydf['NEWYORK終値']
newyork = newyork.apply(lambda x: x.replace(',','')).astype(np.float)
usdjpy = mydf['USDJPY終値']

#データを準備
L = 365
W = 4
newdf = pd.DataFrame(index=mydf.index, columns=[])
Y = nikkei[W-1:N]
for i in range(1,W):
    newdf['x'+str(i)] = nikkei.shift(i).T
newdf['newyork'] = newyork.shift(1).T
newdf['usdjpy'] = usdjpy.shift(1).T
X = newdf[W-1:N]

#モデルを指定
model = linear_model.LinearRegression()

#モデル学習と予測の繰り返し
M = 570
Ytest = np.empty(M)
Ypred = np.empty(M)
Ydate = []
for m in range(M):
    #モデルの学習
    xtrain = X[m:m+L]
    ytrain = Y[m:m+L]
    model.fit(xtrain,ytrain)
    #モデルによるYの予測値を計算
    Ytest[m] = Y[m+L:m+L+1]
    ydate=str(Y.index[m+L]).split()[0]
    Ydate.append(ydate)
    xtest = X[m+L:m+L+1]
    ypred = model.predict(xtest)
    Ypred[m] = ypred[0]
    print("ydate =%s ytest =%9.2f ypred =%9.2f" % (Ydate[m], Ytest[m], Ypred[m]))

#評価指標MSE
mse = metrics.mean_squared_error(Ytest, Ypred)
print("MSE=", mse)
mae = np.sum(np.abs(Ypred-Ytest))/M
print("MAE=", mae)
msre = np.dot((Ypred-Ytest)/Ytest, (Ypred-Ytest)/Ytest)/M
print("MSRE=", msre)
mare = np.sum(np.abs(Ypred-Ytest)/Ytest)/M
print("MARE=", mare)

# グラフ表示
plt.title('Prediction of Nikkei (Price)')
plt.xlabel('date')
plt.ylabel('price')
plt.grid()
plt.plot(Ytest, color='blue')
plt.plot(Ypred,color='red')
plt.show()
