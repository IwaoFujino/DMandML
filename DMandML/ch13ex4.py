# カラー画像
import cv2.cv2 as cv

# カラー画像データのロード
img1 = cv.imread('./imagedata/image3.jpg')
print("カラー画像のサイズ：", img1.shape)
# リサイズ画像
w = 12
h = 7
img2 = cv.resize(img1,(w,h))
print("リサイズ画像のサイズ：", img2.shape)
print("赤（R):")
for row in img2[:, :, 0]:
    for data in row:
        print(data, " ", end="")
    print()
print("緑（G):")
for row in img2[:, :, 1]:
    for data in row:
        print(data, " ", end="")
    print()
print("青（B):")
for row in img2[:, :, 2]:
    for data in row:
        print(data, " ", end="")
    print()
