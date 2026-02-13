#ライブラリを持ってくる
import sqlite3
import csv

#ライブラリにあるdbに接続するモジュールを使う※なければファイルを新規作成
db = sqlite3.connect("sample.db")
print("データベースに接続しました。")

#データベースを操作するためのモジュールを使う
cur = db.cursor()

#表作成する
cur.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER , others TEXT)""")

name = input("名前を入力:")
age = int(input("年齢を入力:"))
others = input("趣味:")

cur.execute("INSERT INTO users(name, age , others)VALUES(?, ? ,?)",(name , age ,others))

db.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()

with open("sample.csv","w",newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id","name","age","others"])
    writer.writerows(rows)

cur.close()

#生成されたデータベースの接続を終了する※クローズさせないと永久に動き続ける
db.close()
print("データベースとの接続を閉じました。")