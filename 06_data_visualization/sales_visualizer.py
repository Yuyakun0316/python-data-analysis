import pandas as pd
import matplotlib.pyplot as plt

# 1. 練習用のCSVファイル
csv_data = """月,売上
1月,100000
2月,120000
3月,180000
4月,150000
5月,200000
6月,250000
"""
with open("sales_data.csv", "w", encoding="utf-8") as f:
    f.write(csv_data)

# 2. 【読み込み】CSVファイルをpandasで読み込む
df = pd.read_csv("sales_data.csv")