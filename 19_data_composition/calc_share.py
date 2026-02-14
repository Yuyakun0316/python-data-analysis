import pandas as pd

# 1. 地域別売上データ
data = {
    "地域": ["関東", "関西", "中部", "九州", "東北"],
    "売上": [500000, 300000, 150000, 100000, 50000]
}
df = pd.DataFrame(data)

# 2. 売上の合計を計算する
total_sales = df["売上"].sum()

# 3. 各地域の構成比（％）を計算する
# 小数点第1位で四捨五入（round）
df["構成比(%)"] = (df["売上"] / total_sales * 100).round(1)

# 4. 保存
df.to_excel("sales_share_report.xlsx", index=False)

print("地域別の売上構成比の計算が完了しました！")
print(df)