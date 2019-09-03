# ORB特徴量＋キーポイントを表示
import cv2.cv2 as cv

# 画像ファイルの読み込み
img = cv.imread('./imagedata/image6.jpg')
img=cv.resize(img,(600,400))
# ORB特徴量検出器
detector = cv.ORB_create()
# 特徴点と特徴量検出
kp, des = detector.detectAndCompute(img, None)
print("特徴量：")
print(des)
print("特徴量のサイズ：")
print(des.shape)
print("特徴量のデータタイプ：")
print(des.dtype)
# 画像への特徴点の書き込み
imgkp = cv.drawKeypoints(img, kp, None)
# 画像表示
cv.imshow("keypoints", imgkp)

cv.waitKey(0)
cv.destroyAllWindows()
