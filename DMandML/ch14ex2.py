# 特徴量の抽出と類似判別
# 特徴量：AKAZE
import cv2.cv2 as cv
import numpy as np
import datetime

#画像の特徴量を計算
def extract_features():
    # 画像ファイルの読み込み
    img0 = cv.imread('./imagedata/image0.jpg')
    img1 = cv.imread('./imagedata/image1.jpg')
    img2 = cv.imread('./imagedata/image2.jpg')
    img3 = cv.imread('./imagedata/image3.jpg')
    # 特徴検出器
    detector = cv.AKAZE_create()
    # 特徴検出
    kp0, des0 = detector.detectAndCompute(img0, None)
    kp1, des1 = detector.detectAndCompute(img1, None)
    kp2, des2 = detector.detectAndCompute(img2, None)
    kp3, des3 = detector.detectAndCompute(img3, None)
   
    return des0, des1, des2, des3

# 画像の一致する特徴点の平均距離
def calculate_ave_dist(desa,desb):
    bf = cv.BFMatcher()
    matches = bf.match(desa, desb)
    matches = sorted(matches, key = lambda x : x.distance)
    nn=int(len(matches)/100)
    dists = [m.distance for m in matches[0:nn]]
    aved = sum(dists)/len(dists)

    return aved

# 計算結果を表示
def print_result(result):
    docno = ["画像0", "画像1 ", "画像2 ", "画像3 "]
    print("画像No  ", end='')
    for n in docno:
        print("%6s  " % n, end='')
    print()
    for n, res in zip(docno, result):
        print("%s" % n, end='')
        for r in res:
            print("%10.2f" % r, end='')
        print()

    return

# メイン処理
def main():
    descs = extract_features()
    avedist = np.empty([4,4], dtype=np.float)
    for i in range(4):
        for j in range(4):
            avedist[i,j] = calculate_ave_dist(descs[i], descs[j])
    print_result(avedist)

    return

# ここから実行する
if __name__ == "__main__":
	start_time = datetime.datetime.now()
	main()
	end_time = datetime.datetime.now()
	elapsed_time = end_time - start_time
	print("経過時間=", elapsed_time)
	print("すべて完了 !!!")
