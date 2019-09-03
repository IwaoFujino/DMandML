#　NIKKEI前日比データ作成、グラフ表示
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSVファイル読み込み
mydf = pd.read_csv('NIKKEI20152018.csv', index_col=0, parse_dates=[0])
mydf = mydf.sort_index()
temp = mydf['NIKKEI前日比%']
temp = temp.apply(lambda x: x.replace('%','')).astype(np.float)/100.0
print(temp.head())
N = len(temp)
print("N=",N)

# グラフ表示
plt.title('NIKKEI 2015-2018')
plt.xlabel('date')
plt.ylabel('ratio')
plt.grid()
plt.plot(temp.values, color='blue')
plt.show()
