# 時系列データのデータフレーム、ダウンサンプリングとグラフ表示
import pandas as pd
import matplotlib.pyplot as plt

# CSVファイル読み込み
mydf = pd.read_csv('TokyoTemp20082017.csv',
         index_col=0, parse_dates=[0], dtype='float')

print(mydf.describe())
print(mydf.head())
print(mydf.index)

mydf_down = mydf.resample('Y').mean() 
mydf_down = mydf_down.rename(columns={'Temp(C)': 'Temp_YearMean(C)'})
print(mydf_down)

# グラフ表示
fig = mydf.plot(title='Tokyo Temperature Data Set', figsize=(8,5))
mydf_down.plot(ax=fig) 
plt.show()
