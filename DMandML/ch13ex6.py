# 特徴量の抽出と画像間チング
# 特徴量：ORB
import cv2.cv2 as cv

# 画像ファイルの読み込み
img1 = cv.imread('./imagedata/image6.jpg')
img1 = cv.resize(img1,(600,400))
img2 = cv.imread('./imagedata/image2.jpg')
img2 = cv.resize(img2,(600,400))
# ORB特徴検出器
detector = cv.ORB_create()
# 特徴量抽出
kp1, des1 = detector.detectAndCompute(img1, None)
kp2, des2 = detector.detectAndCompute(img2, None)
bf = cv.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)
#マッチングリスト 
matched = []
for match1, match2 in matches:
        ratio = match1.distance/match2.distance
        if ratio < 0.8:
                matched.append([match1])
 # 画像表示
imgmatches = cv.drawMatchesKnn(img1,kp1,img2,kp2,matched,None,flags=2)
cv.imshow("image matching", imgmatches)

cv.waitKey(0)
cv.destroyAllWindows()
