# ディクショナリ操作のメソッド
# 繰り返しfor文＋ディクショナリ

pp={"山田":45, "佐藤":67, "田中":38, "木村":87, "鈴木":56, "村田":78, "山下":91, "小島":45}


print("for文を使って、全要素を表示：")
for key, value in pp.items():
    print("名前=",key, "点数=",value)

print("for文を使って、すべての名前を表示：")
for name in pp.keys():
    print("名前=",name)

print("for文を使って、すべての点数を表示：")
for score in pp.values():
    print("点数=",score)
