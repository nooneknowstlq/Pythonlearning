import sqlite3

with sqlite3.connect("dzalchemy.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS mans(
        man_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        profession TEXT,
        age INTEGER
    )""")

    cur.execute("INSERT INTO mans VALUES(1, 'Федор', 'Пупкин', 'Повар', 26)")
    cur.execute("INSERT INTO mans VALUES(2, 'Григорий', 'Микушин', 'ребенок', 1)")
    cur.execute("INSERT INTO mans VALUES(3, 'Криштиану', 'Роналду', 'Футболист', 36)")
    cur.execute("INSERT INTO mans VALUES(4, 'Кот', 'Матроскин', 'Матрос', 12)")
    cur.execute("INSERT INTO mans VALUES(5, 'Игорь', 'Печкин', 'Почтальон', 54)")
    cur.execute("INSERT INTO mans VALUES(6, 'Владимир', 'Путин', 'Президент', 71)")
    cur.execute("INSERT INTO mans VALUES(7, 'Кира', 'Найтли', 'Актриса', 38)")
    cur.execute("INSERT INTO mans VALUES(8, 'Василий', 'Уткин', 'Комментатор', 51)")

# con.commit()
# con.close()
