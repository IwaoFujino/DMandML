#線形回帰モデル
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn import linear_model
from sklearn import model_selection
from sklearn import metrics

#データを準備
boston = load_boston()
#print(boston['DESCR'])
#print(boston['data'])
#print(boston['feature_names'])
X = pd.DataFrame(boston['data'], columns = boston['feature_names'])
Y = pd.DataFrame(boston['target'])
#print("X_info=",X.info)
#print("Y_info=",Y.info)

#モデルを指定
clf =linear_model.LinearRegression()

#データを訓練セットとテストセットに分割
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.3)
print("訓練データサイズ：（説明変数)（目的変数)")
print(X_train.shape, Y_train.shape)
print("テストデータサイズ：（説明変数)（目的変数)")
print(X_test.shape, Y_test.shape)

#モデルの学習
clf.fit(X_train, Y_train)
print("回帰係数=", clf.coef_)
print("切片=", clf.intercept_)
print("決定係数=", clf.score(X_train, Y_train))

#モデルによるYの予測値を計算
print("テストセットによる決定係数=", clf.score(X_test, Y_test))
Yp = clf.predict(X_test)
mse = metrics.mean_squared_error(Y_test, Yp)
print("テストセットによるMSE=", mse)
