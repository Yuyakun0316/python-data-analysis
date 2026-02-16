import pandas as pd

# 1. 売上データ（縦長のリスト）
data = {
    "月": ["1月", "1月", "2月", "2月", "1月", "2月"],
    "支店": ["東京", "大阪", "東京", "大阪", "東京", "大阪"],
    "売上": [100, 150, 200, 120, 80, 130]
}
df = pd.DataFrame(data)

# 2. ピボットテーブルを作成
# 縦に「支店」、横に「月」を並べて、売上の合計を出す
pivot_df = df.pivot_table(
    values="売上", 
    index="支店", 
    columns="月", 
    aggfunc="sum",
    fill_value=0 # データがない場合は0にする
).reset_index()

# 3. 保存
pivot_df.to_excel("sales_pivot_table.xlsx", index=False)

print("ピボットテーブルの作成が完了しました！")
print(pivot_df)