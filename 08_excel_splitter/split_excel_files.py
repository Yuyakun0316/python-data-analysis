import pandas as pd
import os

# 1. 練習用の「全社売上データ」を作成
data = [
    {"支店": "東京", "商品": "PC", "売上": 100000},
    {"支店": "大阪", "商品": "マウス", "売上": 5000},
    {"支店": "東京", "商品": "モニター", "売上": 30000},
    {"支店": "福岡", "商品": "PC", "売上": 120000},
    {"支店": "大阪", "商品": "キーボード", "売上": 8000},
]
df = pd.DataFrame(data)

# 2. 保存用フォルダ「output」を作成（すでにあれば何もしない）
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# 3. 【重要】「支店」の種類を抜き出す（東京、大阪、福岡）
branches = df["支店"].unique()
print(f"分割する支店リスト: {branches}")

# 4. 【分割】支店ごとにデータを絞り込んで保存する
for branch in branches:
    # その支店だけのデータに絞り込む
    branch_df = df[df["支店"] == branch]
    
    # ファイル名を作って保存（output/東京.xlsx など）
    file_path = os.path.join(output_dir, f"{branch}.xlsx")
    branch_df.to_excel(file_path, index=False)
    print(f"作成完了: {file_path}")

print("すべての支店別ファイルの分割が完了しました！")