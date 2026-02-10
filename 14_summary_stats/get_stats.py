import pandas as pd

# 1. 適当な点数データ
df = pd.DataFrame({
    "テスト点数": [80, 95, 70, 100, 60, 85, 90],
    "勉強時間": [2, 4, 1, 5, 1, 3, 4]
})

# 2. データの要約（平均・最大・最小など）を一気に出す
stats = df.describe()

# 3. 保存
stats.to_excel("summary_stats.xlsx")