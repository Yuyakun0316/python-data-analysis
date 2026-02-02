import pandas as pd

# 1. 支店ごとの売上明細データ
raw_data = [
    {"支店": "東京本店", "担当": "田中", "売上": 100000},
    {"支店": "大阪支店", "担当": "佐藤", "売上": 150000},
    {"支店": "東京本店", "担当": "鈴木", "売上": 80000},
    {"支店": "福岡支店", "担当": "高橋", "売上": 200000},
    {"支店": "大阪支店", "担当": "伊藤", "売上": 120000},
    {"支店": "東京本店", "担当": "山本", "売上": 50000},
]
df = pd.DataFrame(raw_data)

# 2. 【集計】支店ごとに「売上の合計」と「取引件数」を計算する
# これがExcelのピボットテーブルと同じ役割
summary_df = df.groupby("支店")["売上"].agg(["sum", "count"]).reset_index()

# 3. 【名前変更】列名を分かりやすく「合計売上」「取引件数」に変える
summary_df.columns = ["支店名", "合計売上", "取引件数"]

# 4. 【並び替え】合計売上が高い順に並べる
summary_df = summary_df.sort_values(by="合計売上", ascending=False)

# 5. 保存
summary_df.to_excel("branch_summary_report.xlsx", index=False)

print("支店別集計レポートの作成が完了しました！")
print(summary_df)