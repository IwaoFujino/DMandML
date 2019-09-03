# SVM法による分類(irisデータセット)
from sklearn import datasets
from sklearn import model_selection
from sklearn import svm
from sklearn import metrics

#　データを取得
iris = datasets.load_iris()
data_train, data_test, label_train, label_test = model_selection. train_test_split(iris['data'], iris['target'], test_size=0.25)

# モデルを作成
# ペナルティパラメータ
C = 1000
# RBFカーネルのパラメータ
gamma = 10
model = svm.SVC(C=C, gamma=gamma)
model.fit(data_train, label_train)

#　データを分類
label_train_pred = model.predict(data_train)
label_test_pred = model.predict(data_test)

# 分類結果の評価
print("訓練データによる評価:")
print("精度 =", metrics.accuracy_score(label_train, label_train_pred))
print(metrics.classification_report(label_train, label_train_pred, target_names=iris['target_names']))
print("テストデータによる評価:")
print("精度 =", metrics.accuracy_score(label_test, label_test_pred))
print(metrics.classification_report(label_test, label_test_pred, target_names=iris['target_names']))
