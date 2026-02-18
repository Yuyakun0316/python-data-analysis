import pandas as pd

# 1. 「文字列」の日付データ
data = {
    "イベント": ["キャンペーン開始", "中間発表", "最終締め切り"],
    "日付文字列": ["2024-01-01", "2024-02-15", "2024-03-31"]
}
df = pd.DataFrame(data)

# 2. 文字列を「datetime型（日付型）」に変換する
# これをやらないと、日付としての計算や並び替えがうまくできません
df["日付"] = pd.to_datetime(df["日付文字列"])

# 3. 日付から「曜日」を抽出する
df["曜日"] = df["日付"].dt.day_name()

# 4. 土日かどうかを判定するフラグ
# 曜日が Saturday か Sunday なら True
df["週末フラグ"] = df["曜日"].isin(["Saturday", "Sunday"])

# 5. 保存
df.to_excel("event_schedule.xlsx", index=False)

print("日付データの加工が完了しました！")
print(df[["イベント", "日付", "曜日", "週末フラグ"]])