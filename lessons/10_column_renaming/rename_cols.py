import pandas as pd

# 1. 練習用の英語データ（システムから出た設定）
df = pd.DataFrame({
    "user_id": ["ID_01", "ID_02"],
    "order_date": ["2024-01-01", "2024-01-02"],
    "price": [1500, 3000]
})

# 2. 名前の対応表（辞書）を作る
name_map = {
    "user_id": "ユーザーID",
    "order_date": "注文日",
    "price": "金額"
}

# 3. 名前を書き換える
df = df.rename(columns=name_map)

# 4. 保存
df.to_excel("formatted_report.xlsx", index=False)

print("列名の日本語化が完了しました！")
print(df)