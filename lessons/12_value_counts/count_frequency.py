import pandas as pd

# 1. 練習用のアンケートデータ（好きな果物アンケート）
data = {
    "名前": ["田中", "佐藤", "鈴木", "高橋", "伊藤", "渡辺", "山本", "中村"],
    "好きな果物": ["りんご", "バナナ", "りんご", "メロン", "バナナ", "りんご", "オレンジ", "バナナ"]
}
df = pd.DataFrame(data)

# 2. どの果物が何個選ばれたかを集計する
# SQLで言う COUNT(*) GROUP BY 好きな果物 
fruit_counts = df["好きな果物"].value_counts()

# 3. 保存
# value_countsの結果は「シリーズ」という形式なので、to_excelでそのまま保存できる
fruit_counts.to_excel("fruit_frequency.xlsx")

print("出現頻度の集計が完了しました！")
print(fruit_counts)