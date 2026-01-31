import pandas as pd

# 1. 練習用のデータ（本来はPDFから抜いたデータが入る場所）
data = [
  {"ファイル名": "sample1", "請求金額" : "11000", "件名": "4月分"},
  {"ファイル名": "sample2", "請求金額" : "22000", "件名": "5月分"},
  {"ファイル名": "sample3", "請求金額" : "33000", "件名": "6月分"}
]

# 2. pandasの「データフレーム」に変換
df = pd.DataFrame(data)

# 3. 【お掃除】金額を「文字」から「数字」に変える（計算できるようにするため）
df["請求金額"] = df["請求金額"].astype(int)

# 4. 【集計】合計金額を計算する
total_price = df["請求金額"].sum()

# 5. 【整理】新しい行（合計行）を追加してみる
total_row = pd.DataFrame([{
  "ファイル名": "合計", 
  "請求金額": total_price, 
  "件名": "-", 
  }])
df = pd.concat([df, total_row], ignore_index=True)

# 6. Excelに書き出す
df.to_excel("summary_report.xlsx", index=False)

print("pandasでの集計とExcel保存が完了しました！")
print(df)