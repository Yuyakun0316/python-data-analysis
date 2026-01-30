import pandas as pd

#1. データの読み込み
df = pd.read_csv("sales.csv")

#2. 前準備：「売上金額」列を作る
# 単価 ＊ 個数 ＝ 売上
df["売上金額"] = df["単価"] * df["個数"]

#中身を確認
print("--- 計算後のデータ ---")
print(df)

#3. 日付ごとの売り上げ合計を出す(GROUP BY)
# SQL: SELECT 日付, SUM(売上金額) FROM sales GROUP BY 日付;
print("\n--- 日付売上レポート ---")

# groupby("まとめる列")["計算したい列"].sum()
dailiy_sales = df.groupby("日付")["売上金額"].sum()

print(dailiy_sales)

# 4. 一番売れた日を知る (Sort)
print("\n--- 最も売れた日 ---")
print(dailiy_sales.sort_values(ascending=False)) # 降順（高い順）に並び替え)