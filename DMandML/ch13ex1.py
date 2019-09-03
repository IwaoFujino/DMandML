# 手書き数字データセットdigits
from sklearn import datasets
import matplotlib.pyplot as plt

digits = datasets.load_digits()
# データを確認
print("属性名:")
for key in digits.keys():
    print(key)
print("ベクトルデータ：")
print(digits['data'][:2])
print("ベクトルデータのユニークな値：")
for i in range(3):
    print(list(set(digits['data'][i])))
mm, nn = digits['data'].shape
print("行数=", mm, "列数=", nn)
print("画像データ：")
print(digits['images'][:2])
ii, mm, nn = digits['images'].shape
print("番号=", ii, "行数=", mm, "列数=", nn)
print("ラベルデータ")
print(digits['target'][:20])
ii = len(digits['target'])
print("ラベルデータ数=", ii)
print("ラベル名")
print(digits['target_names'])
mm = len(digits['target_names'])
print("ラベル数=", mm)

# 画像サンプルを20個表示
plt.subplots_adjust(wspace=0.4, hspace=0.6)
for i in range(20):
    plt.subplot(4, 5, i + 1)
    plt.imshow(digits['images'][i], cmap='gray', interpolation='None')
    plt.axis('off')
    plt.title('Label=%i' % digits['target'][i])

plt.show()
