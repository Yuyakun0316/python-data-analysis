import pandas as pd
import numpy as np # 条件分岐に便利なライブラリ

# 1. 商品データ
data = {
    "商品名": ["ノートPC", "マウス", "キーボード", "モニター", "USBメモリ"],
    "単価": [120000, 3000, 8000, 25000, 1500]
}
df = pd.DataFrame(data)

# 2. 単価が 10,000円 以上なら「高額品」、そうでなければ「消耗品」とラベルを貼る
# np.where(条件, 真の時の値, 偽の時の値) という書き方
df["区分"] = np.where(df["単価"] >= 10000, "高額品", "消耗品")

# 3. さらに複雑な条件（5万以上なら「要承認」）のフラグ
df["要承認フラグ"] = np.where(df["単価"] >= 50000, "要確認", "-")

# 4. 保存
df.to_excel("product_classification.xlsx", index=False)

print("条件によるラベル付けが完了しました！")
print(df)