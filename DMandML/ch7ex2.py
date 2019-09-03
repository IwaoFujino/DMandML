# Naive Bayes法による分類(離散値)
import numpy as np
from sklearn import datasets
from sklearn import model_selection
from sklearn import naive_bayes
from sklearn import metrics

#　データの生成
datalen=100
Xdata = np.random.randint(2, size=(datalen, 20))
Ydata = np.random.randint(4, size=datalen)
Ylabel=sorted(list(set(map(str, Ydata))))
print("特徴量データ=",Xdata)
print("ラベルデータ=",Ydata)
print("ラベルリスト=",Ylabel)

data_train, data_test, label_train, label_test = model_selection.train_test_split(Xdata, Ydata, test_size=0.25)

# モデル作成
model = naive_bayes.BernoulliNB()
model.fit(data_train, label_train)

#　データを分類
y_true = label_test
y_pred = model.predict(data_test)
print("真ラベル =", y_true)
print("予測ラベル =", y_pred)

# 分類結果の評価
print("精度 =", metrics.accuracy_score(y_true, y_pred))
print(metrics.classification_report(y_true, y_pred, target_names=Ylabel))
