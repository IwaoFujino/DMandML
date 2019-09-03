# OpenCVの簡単な例
import cv2.cv2 as cv

# カラー画像データのロード
img1 = cv.imread('./imagedata/image3.jpg')
print("カラー画像のサイズ：", img1.shape)
cv.imshow("original image", img1)
cv.waitKey(0)
cv.destroyAllWindows()

# モノクロ画像
img2= cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
print("モノクロ画像のサイズ：", img2.shape)
cv.imshow("gray image", img2)
cv.waitKey(0)
cv.destroyAllWindows()

# トリミング画像
img3=img1[500:2620,300:3460]
print("トリミング画像のサイズ：", img3.shape)
cv.imshow("trimmed image", img3)
cv.waitKey(0)
cv.destroyAllWindows()

# リサイズ画像
img4=cv.resize(img1,(300,200))
print("リサイズ画像のサイズ：", img4.shape)
cv.imshow("resized image", img4)
cv.waitKey(0)
cv.destroyAllWindows()
