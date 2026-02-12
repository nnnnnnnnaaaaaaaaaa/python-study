import sqlite3

# データベース作成（なければ新しく作られる）
conn = sqlite3.connect("mountain.db")

cursor = conn.cursor()

# テーブル作成
cursor.execute("""
CREATE TABLE IF NOT EXISTS mountains (
    id INTEGER PRIMARY KEY,
    name TEXT,
    height INTEGER
)
""")

# データ追加
cursor.execute("INSERT INTO mountains (name, height) VALUES (?, ?)", ("Fuji", 3776))

#削除
#cursor.execute("DELETE FROM mountains WHERE name = ?", ("Fuji",))

# 保存
conn.commit()

# データ取得
cursor.execute("SELECT * FROM mountains WHERE height > ?", (3000,))
rows = cursor.fetchall()



print(rows)

conn.close()
