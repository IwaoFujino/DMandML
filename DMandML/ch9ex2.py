# 線形回帰モデルによる時系列データの予測
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

# CSVファイル読み込み
mydf = pd.read_csv('TokyoTemp20082017.csv', index_col=0, parse_dates=[0], dtype='float')

#データを準備
temp = mydf['Temp(C)']
N = len(temp)
print("N=",N)
L = 365
Y = temp.shift(0)[7:N]
x1 = temp.shift(1)[7:N]
x2 = temp.shift(2)[7:N]
x3 = temp.shift(3)[7:N]
x4 = temp.shift(4)[7:N]
x5 = temp.shift(5)[7:N]
x6 = temp.shift(6)[7:N]
x7 = temp.shift(7)[7:N]
X =pd.DataFrame([x1, x2, x3, x4, x5, x6, x7]).T

#データを表示
for n in range(10):
    print("n=",n,"\t Y=", Y[n],"\t X=", x1[n],x2[n],x3[n],x4[n],x5[n],x6[n],x7[n])

#モデルを指定
model = linear_model.LinearRegression()

#モデルの学習
model.fit(X[0:L],Y[0:L])
print("回帰係数=", model.coef_)
print("切片=", model.intercept_)
print("決定係数=", model.score(X[0:L],Y[0:L]))

#モデルによるYの予測値を計算
ytest = Y[L:L+1]
print("ytest=",ytest)
xtest = X[L:L+1]
print("xtest=",xtest)
ypred = model.predict(xtest)
print("ypred=",ypred[0])
