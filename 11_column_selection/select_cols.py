import pandas as pd

# 1. たくさん列があるデータ
df = pd.DataFrame({
    "ID": [101, 102],
    "名前": ["田中", "佐藤"],
    "住所": ["東京", "大阪"],
    "電話番号": ["090-xxx", "080-xxx"],
    "メモ": ["重要", "保留"]
})

# 2. 必要な列名だけをリストで指定して抜き出す
# [ ] の中にもう一つ [ ] を書くのがコツ
selected_df = df[["ID", "名前", "メモ"]]

# 3. 保存
selected_df.to_excel("selected_columns.xlsx", index=False)

print("必要な列の抽出が完了しました！")
print(selected_df)