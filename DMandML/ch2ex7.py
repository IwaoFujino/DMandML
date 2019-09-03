#　二重for文
#  九九の表

for m in range(1,10):
    for n in range(1,10):
        print("%1dx%1d=%2d " % (m, n, m*n), end="")
    print()