# モジュールの利用
import ch3ex3module

# インスタンスの生成    
seito1 = ch3ex3module.seito("山田", 34, 56, 87, 45)
seito1.showdata()
n, k1, k2, k3, k4=seito1.getdata()
ch3ex3module.gouhi(n, k1, k2, k3, k4)
seito2 = ch3ex3module.seito("佐藤", 90, 86, 77, 65)
seito2.showdata()
n, k1, k2, k3, k4=seito2.getdata()
ch3ex3module.gouhi(n, k1, k2, k3, k4)
