import pandas as pd

# 1. 「コード化された」データ
# 1: 営業中, 2: 準備中, 3: 閉店
data = {
    "店舗名": ["東京店", "大阪店", "名古屋店", "福岡店"],
    "ステータスID": [1, 2, 1, 3]
}
df = pd.DataFrame(data)

# 2. 対応表（マッピング辞書）を作る
status_map = {
    1: "営業中",
    2: "準備中",
    3: "閉店"
}

# 3. 新しい列を作って、一気に変換する
df["ステータス名"] = df["ステータスID"].map(status_map)

# 4. 保存
df.to_excel("store_status_report.xlsx", index=False)

print("ステータスのマッピングが完了しました！")
print(df)