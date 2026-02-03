import pandas as pd
import glob # ファイルを探すためのライブラリ

# 1. 練習用のExcelファイルを3つ自動で作る
# ※本来は最初からあるファイルを使う想定
for month in ["01", "02", "03"]:
    temp_df = pd.DataFrame([{"月": f"{month}月", "売上": 100000 * int(month)}])
    temp_df.to_excel(f"2024_{month}_sales.xlsx", index=False)

# 2. 【探し出す】フォルダ内の「sales.xlsx」で終わるファイルをすべて取得
file_list = glob.glob("*_sales.xlsx")
print(f"見つかったファイル: {file_list}")