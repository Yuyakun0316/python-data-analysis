import pandas as pd

# 1. データの読み込み
df = pd.read_csv("sales.csv")

print("=== 全データの表示 ===")
print(df)
print("\n")

# --- 実験1: 特定の列だけ取り出す (SELECT) ---
# SQL: SELECT 商品名, 単価 FROM sales;
# Pandas: df[["列名", "列名"]]  (リストで渡すのがポイント！)
print("=== 商品名と単価だけ表示 ===")
subset = df[["商品名", "単価"]]
print(subset)


# --- 実験2: 条件で絞り込む (WHERE) ---
# SQL: SELECT * FROM sales WHERE 商品名 = 'Tシャツ';
# Pandas: df[ 条件式 ]
print("\n=== Tシャツだけを表示 ===")
t_shirts = df[df["商品名"] == "Tシャツ"]
print(t_shirts)

# SQL: SELECT * FROM sales WHERE 単価 >= 3000;
print("\n=== 単価が3000円以上の商品 ===")
expensive_items = df[df["単価"] >= 3000]
print(expensive_items)


# --- 実験3: データの情報を知る ---
# データ分析では「平均」や「最大値」をよく見ます
print("\n=== 統計情報 ===")
print(f"データの件数: {len(df)}")        # SQL: COUNT(*)
print(f"単価の平均値: {df['単価'].mean()}") # SQL: AVG(単価)
print(f"単価の最大値: {df['単価'].max()}")  # SQL: MAX(単価)

# Q1. 単価が5000円より高い
print("\n--- 5000円より高い商品 ---")
print(df[df["単価"] > 5000])

# Q2. スニーカーだけ
print("\n--- スニーカーだけ ---")
print(df[df["商品名"] == "スニーカー"])

# Q3. 個数が2個以上
print("\n--- 個数が2個以上 ---")
print(df[df["個数"] >= 2])