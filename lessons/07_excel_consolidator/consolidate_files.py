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

# 3. 【読み込み】見つかったファイルを一つずつ読み込んでリストに溜める
all_data = []
for file in file_list:
    df = pd.read_excel(file)
    # ここに「ファイル名」という新しい列を追加して、ファイルの名前を書き込む！
    df["元ファイル名"] = file 
    all_data.append(df)

# 4. 【合体】溜まったデータを縦に一つに繋げる
combined_df = pd.concat(all_data, ignore_index=True)

# 【追加】月できちんと並び替える（01→02→03にする）
combined_df = combined_df.sort_values(by="月")

# 5. 保存
combined_df.to_excel("annual_sales_combined.xlsx", index=False)

print("すべてのExcelファイルの合体が完了しました！")
print(combined_df)