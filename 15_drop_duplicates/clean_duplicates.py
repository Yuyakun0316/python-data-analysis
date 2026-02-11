import pandas as pd

# 1. わざと重複させたデータ（田中さんと佐藤さんが2回ずつ）
data = {
    "名前": ["田中", "佐藤", "田中", "鈴木", "佐藤"],
    "ポイント": [100, 200, 100, 150, 200]
}
df = pd.DataFrame(data)

# 2. 重複した行を削除する
# 全く同じ内容の行が1つにまとまる
clean_df = df.drop_duplicates()

# 3. 保存
clean_df.to_excel("cleaned_data.xlsx", index=False)

print("重複データの削除が完了しました！")
print("元の行数:", len(df))
print("削除後の行数:", len(clean_df))