import pandas as pd
import numpy as np # 条件分岐に便利なライブラリ

# 1. 商品データ
data = {
    "商品名": ["ノートPC", "マウス", "キーボード", "モニター", "USBメモリ"],
    "単価": [120000, 3000, 8000, 25000, 1500]
}
df = pd.DataFrame(data)