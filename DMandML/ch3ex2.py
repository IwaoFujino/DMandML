# クラスの定義と利用

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
        print(self.namae, self.kokugo, self.sansu, self.rika, self.syakai)
        return
    #　平均値を計算、表示
    def showave(self):
        ave=(self.kokugo + self.sansu + self.rika + self.syakai) / 4.0
        print(self.namae, "ave=", ave)
        return

# インスタンスの生成    
seito1=seito("yamada", 34, 56, 87, 45)
seito1.showdata()
seito1.showave()
seito2=seito("sato", 90, 86, 77, 65)
seito2.showdata()
seito2.showave()
