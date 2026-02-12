import pandas as pd

# 1. 「コード化された」データ
# 1: 営業中, 2: 準備中, 3: 閉店
data = {
    "店舗名": ["東京店", "大阪店", "名古屋店", "福岡店"],
    "ステータスID": [1, 2, 1, 3]
}
df = pd.DataFrame(data)
