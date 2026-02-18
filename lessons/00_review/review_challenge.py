import pandas as pd

data = [
    {"商品": "デスク", "単価": 20000, "数量": 1},
    {"商品": "マウス", "単価": 2000, "数量": 3},
    {"商品": "モニター", "単価": 15000, "数量": 2}
]

df = pd.DataFrame(data)

# 2. 売上列の作成
df["売上"] = df["単価"] * df["数量"]

# 3. 1万円以上で抽出
high_value_df = df[df["売上"] >= 10000]

# 4. 抽出した結果の「売上の合計」を計算
total_sales = high_value_df["売上"].sum()
print(f"1万円以上の商品の合計売上: {total_sales}円")
print(high_value_df)