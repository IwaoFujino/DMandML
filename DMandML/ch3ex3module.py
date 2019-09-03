# 関数の定義

# 合否判断
def gouhi(namae, kokugo, sansu, rika, syakai):
    print(namae, ":", end="")
    if kokugo >= 60:
        print("国語合格,", end="")
    else:
        print("国語不合格,", end="")
    if sansu >= 60:
        print("算数合格,", end="")
    else:
        print("算数不合格,", end="")
    if rika >= 60:
        print("理科合格,", end="")
    else:
        print("理科不合格,", end="")
    if syakai >= 60:
        print("社会合格")
    else:
        print("社会不合格")
    return

# クラスの定義
class seito():
    # 初期値の設定
    def __init__(self, namae, kokugo, sansu, rika, syakai):
        self.namae = namae
        self.kokugo = kokugo
        self.sansu = sansu
        self.rika = rika
        self.syakai = syakai
    # データを表示
    def showdata(self):
        print(self.namae, ":国語=", self.kokugo, "算数=", self.sansu, "理科=", self.rika, "社会=", self.syakai)
        return
    #　平均値を計算、表示
    def getdata(self):
        return self.namae, self.kokugo, self.sansu, self.rika, self.syakai
