# 線形回帰モデルによる時系列データの予測 + 評価指標MSE、グラフ表示
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import metrics

# CSVファイル読み込み
mydf = pd.read_csv('TokyoTemp20082017.csv', index_col=0, parse_dates=[0], dtype='float')
temp = mydf['Temp(C)']
N = len(temp)
print("N=",N)

#データを準備
L = 365
W = 7
newdf = pd.DataFrame(index=mydf.index, columns=[])
Y = temp[W:N]
for i in range(1,W+1):
    newdf['x'+str(i)] = temp.shift(i).T
X = newdf[W:N]

#モデルを指定
model = linear_model.LinearRegression()

#モデル学習と予測の繰り返し
M = 3200
Ytest = np.empty(M)
Ypred = np.empty(M)
Ydate = []
for m in range(M):
    #モデルの学習
    xtrain = X[m:m+L]
    ytrain = Y[m:m+L]
    #print(ytrain)
    #print(xtrain)
    model.fit(xtrain,ytrain)
    #print("回帰係数=", model.coef_)
    #print("切片=", model.intercept_)
    #print("決定係数=", model.score(xtrain,ytrain))

    #モデルによるYの予測値を計算
    Ytest[m] = Y[m+L:m+L+1]
    ydate = str(Y.index[m+L]).split()[0]
    Ydate.append(ydate)
    xtest = X[m+L:m+L+1]
    ypred = model.predict(xtest)
    Ypred[m] = ypred[0]
    #print("xtest=", xtest)
    print("ydate=", Ydate[m], "ytest=", Ytest[m], "ypred=", Ypred[m])

#評価指標MSE
mse=metrics.mean_squared_error(Ytest, Ypred)
print("MSE=", mse)

# グラフ表示
plt.title('Prediction of Tokyo Temperature')
plt.xlabel('date number')
plt.ylabel('temperature')
plt.grid()
plt.plot(Ytest, color='blue')
plt.plot(Ypred, color='red')
plt.show()
