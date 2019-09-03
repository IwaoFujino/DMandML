# 関数の定義と呼び出し

# 関数の定義
def nsum(n):
    s = 0
    for k in range(1, n+1):
        s += k
    return s

# 関数の呼び出し
m = 10
ms = nsum(m)
print(m, "までの総和=", ms)
m = 20
ms = nsum(m)
print(m, "までの総和=", ms)