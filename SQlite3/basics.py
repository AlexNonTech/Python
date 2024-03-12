import sqlite3 as sq

with sq.connect('base.db') as con:
    cur = con.cursor()

    #cur.execute(" DROP TABLE IF EXISTS basics ")
    cur.execute(""" CREATE TABLE IF NOT EXISTS basics (
    id INTEGER,
    user TEXT NOT NULL,
    score INTEGER DEFAULT 0
    )""")

    data = []
    names = ['ALex', 'Suzy', 'Stacy', 'Jason', 'Michael']
    for i in range(5):
        data.append((i + 1, names[i], 100*(i + 1)))

    cur.executemany("INSERT INTO basics VALUES (?, ?, ?)", data)

    cur.execute("SELECT * FROM basics")
    entire_db = cur.fetchall()
    print(entire_db)

    cur.execute("SELECT * FROM basics WHERE user=='Suzy'")
    filtered_name = cur.fetchall()
    print(filtered_name)

    cur.execute("SELECT * FROM basics ORDER BY score DESC ")
    ordered_exe = cur.fetchall()
    print(ordered_exe)

    cur.execute("SELECT * FROM basics WHERE score BETWEEN 100 AND 150 ORDER By score DESC ")
    filter_score = cur.fetchall()
    print(filter_score)

    con.commit()
