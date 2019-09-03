# 特徴量の抽出とベクトル量子化とクラスタリング
# 特徴量：AKAZE
import cv2.cv2 as cv
import numpy as np
import datetime
import scipy.cluster
from sklearn.feature_extraction.text import CountVectorizer
import scipy.cluster.hierarchy as hclst
from matplotlib import pyplot as plt 

#画像の特徴量を計算
def extract_features():
    # 画像ファイルの読み込み
    img0 = cv.imread('./imagedata/image0.jpg')
    img1 = cv.imread('./imagedata/image1.jpg')
    img2 = cv.imread('./imagedata/image2.jpg')
    img3 = cv.imread('./imagedata/image3.jpg')
    img4 = cv.imread('./imagedata/image4.jpg')
    img5 = cv.imread('./imagedata/image5.jpg')
    img6 = cv.imread('./imagedata/image6.jpg')
    # 特徴検出器
    detector = cv.AKAZE_create()
    # 特徴検出
    kp0, des0 = detector.detectAndCompute(img0, None)
    kp1, des1 = detector.detectAndCompute(img1, None)
    kp2, des2 = detector.detectAndCompute(img2, None)
    kp3, des3 = detector.detectAndCompute(img3, None)
    kp4, des4 = detector.detectAndCompute(img4, None)
    kp5, des5 = detector.detectAndCompute(img5, None)
    kp6, des6 = detector.detectAndCompute(img6, None)
   
    return des0, des1, des2, des3, des4, des5, des6

# データをクラスタリング
def create_docs(des0, des1, des2, des3, des4, des5, des6):
    desall = np.vstack((des0, des1, des2, des3, des4,des5, des6))
    npdesall = np.array(desall, dtype='float64')
    codebook, destortion = scipy.cluster.vq.kmeans(npdesall, 100, iter=30, thresh=1e-06)
    # ベクトル量子化
    # 各データをセントロイドに分類する
    code0, dist0 = scipy.cluster.vq.vq(des0, codebook)
    code1, dist1 = scipy.cluster.vq.vq(des1, codebook)
    code2, dist2 = scipy.cluster.vq.vq(des2, codebook)
    code3, dist3 = scipy.cluster.vq.vq(des3, codebook)
    code4, dist4 = scipy.cluster.vq.vq(des4, codebook)
    code5, dist5 = scipy.cluster.vq.vq(des5, codebook)
    code6, dist6 = scipy.cluster.vq.vq(des6, codebook)
    codeall = [code0, code1, code2, code3, code4, code5, code6]
    # コードの文書集合を作成
    docs = []
    for codes in codeall:
        words = ""
        for code in codes:
            words = words+" "+str(code)
        docs.append(words)

    return docs

# コードベクトル作成、クラスタリング
def clustering_images(docs):
    # コードの出現回数のデータを作成
    npdocs = np.array(docs)
    vectorizer = CountVectorizer()
    vecs = vectorizer.fit_transform(npdocs)
    data = vecs.toarray()
     # コードの出現回数のデータを表示
    for no, dd in enumerate(data):
        print("画像番号 =", no)
        print("コードの出現回数データ =")
        for n, d in enumerate(dd):
            if((n+1)%15!=0):
                print("%4d" % d, end="")
            else:
                print("%4d" % d)
        print()
    # クラスタリングは以下3行中の 1 行だけ。
    #results = hclst.linkage(data, method='single',metric='euclidean')
    #results = hclst.linkage(data, method='complete',metric='euclidean')
    results = hclst.linkage(data, method='ward',metric='euclidean')
    # デンドログラムで結果を表示
    hclst.dendrogram(results)
    plt.title("Dendrogram of Clustering Images")
    plt.xlabel("image number")
    plt.ylabel("distance")
    plt.savefig("ch14ex4Figure1.png")

    return

# メイン処理
def main():
    des1, des2, des3, des4, des5, des6, des7 = extract_features()
    docs = create_docs(des1, des2, des3, des4, des5, des6, des7)
    clustering_images(docs)

    return

# ここから実行する
if __name__ == "__main__":
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    elapsed_time = end_time-start_time
    print("経過時間 =", elapsed_time)
    print("すべて完了 !!!")
