import pandas as pd  # ライブラリを読み込む（pdというあだ名をつけるのが慣習）

# 1. CSVファイルを読み込む
# SQL: SELECT * FROM sales;
df = pd.read_csv("sales.csv")

print("--- 1. データの表示 ---")
print(df)

# 2. 「売上（単価 × 個数）」を計算して新しい列を作る
# SQL: SELECT ..., (price * quantity) AS total_price FROM ...
df["売上金額"] = df["単価"] * df["個数"]

print("\n--- 2. 売上計算後 ---")
print(df)

# 3. 商品ごとの合計売上を集計する
# SQL: SELECT product_name, SUM(total_price) FROM ... GROUP BY product_name
grouped = df.groupby("商品名")["売上金額"].sum()

print("\n--- 3. 商品別売上ランキング ---")
print(grouped.sort_values(ascending=False)) # 降順（高い順）に並び替え