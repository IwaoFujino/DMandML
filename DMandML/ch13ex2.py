# SVM法による分類(digitsデータセット)
from sklearn import datasets
from sklearn import model_selection
from sklearn import metrics
from sklearn import svm

#　データを取得
digits = datasets.load_digits()
data_train, data_test, label_train, label_test = model_selection. train_test_split(digits['data'], digits['target'], test_size=0.5)
targetnames=[]
for name in digits['target_names']:
    targetnames.append(str(name))

# モデルを作成
# ペナルティパラメータ
C = 100
# RBFカーネルのパラメータ
gamma = 0.001
model = svm.SVC(C=C, gamma=gamma)
model.fit(data_train, label_train)

#　データを分類
label_train_pred = model.predict(data_train)
label_test_pred = model.predict(data_test)

# 分類結果の評価
print("訓練データによる分類結果：")
print("精度=", metrics.accuracy_score(label_train, label_train_pred))
print(metrics.classification_report(label_train, label_train_pred, target_names=targetnames))
print()
print("テストデータによる分類結果：")
print("精度=", metrics.accuracy_score(label_test, label_test_pred))
print(metrics.classification_report(label_test, label_test_pred, target_names=targetnames))
