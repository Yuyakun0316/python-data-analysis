import pandas as pd
from datetime import datetime

# 1. 適当なデータを用意（昨日のコードの切れ端でOK）
df = pd.DataFrame({"項目": ["学習", "休息", "睡眠"], "状態": ["完了", "進行中", "予定"]})

# 2. 今の時刻を「2024-02-01 10:00:00」のような形式で取得
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")