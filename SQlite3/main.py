import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)"):

# res = cur.execute("SELECT name from sqlite_master WHERE name='spam'")
# print(res.fetchone() is None)

# cur.execute("""
#     INSERT INTO movie VALUES
#     ('Monty Python and the Holy Grail', 1975, 8.2),
#     ('And now for Something Completely Different', 1971, 7.5)
# """)

# con.commit()

# res = cur.execute("SELECT * FROM movie")
# print(res.fetchall())

# data = [
#     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
#     ("Monty Python's The Meaning of Life", 1983, 7.5),
#     ("Monty Python's Life of Brian", 1979, 8.0),
# ]
#
# cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
# con.commit()

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

con.close()
