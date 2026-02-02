import pandas as pd

# 1. 「売上履歴」データ（誰がいくら買ったか）
sales_data = [
    {"顧客ID": "C001", "商品": "ノートPC", "売上": 120000},
    {"顧客ID": "C002", "商品": "マウス", "売上": 3000},
    {"顧客ID": "C001", "商品": "モニター", "売上": 25000},
    {"顧客ID": "C003", "商品": "キーボード", "売上": 8000},
]
df_sales = pd.DataFrame(sales_data)

# 2. 「顧客マスタ」データ（顧客IDと名前の対応表）
customer_master = [
    {"顧客ID": "C001", "名前": "田中商事", "地域": "東京"},
    {"顧客ID": "C002", "名前": "佐藤産業", "地域": "大阪"},
    {"顧客ID": "C003", "名前": "鈴木商店", "地域": "福岡"},
]
df_customers = pd.DataFrame(customer_master)

# 3. 【合体】顧客IDをキーにして、売上データに名前を紐付ける（VLOOKUPと同じ）
df_merged = pd.merge(df_sales, df_customers, on="顧客ID", how="left")

# 4. 【整理】「地域」の情報はいらないので消しちゃおう
df_final = df_merged.drop(columns=["地域"])

# 5. 保存
df_final.to_excel("final_sales_report.xlsx", index=False)

print("データの紐付けと整理が完了しました")
print(df_final)