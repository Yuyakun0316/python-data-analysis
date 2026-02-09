import pandas as pd

# 1. データ
df = pd.DataFrame({
    "名前": ["忍者", "わんこ"],
    "ポイント": [100, 200]
})

# 2. 複数の形式で保存する
# Excel形式で保存
df.to_excel("result.xlsx", index=False)

# CSV形式で保存（カンマ区切りのテキストファイル）
# encoding="utf-8-sig" をつけるとExcelで開いても文字化けしない
df.to_csv("result.csv", index=False, encoding="utf-8-sig")

print("ExcelとCSVの両方で保存が完了しました！")