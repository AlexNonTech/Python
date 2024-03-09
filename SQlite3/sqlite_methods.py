import sqlite3

con = sqlite3.connect("tutorial.db")

cur = con.cursor()
query = input("Enter you db query: ")

if sqlite3.complete_statement(f"{query}" + ";"):
    try:
        res = cur.execute(query)
        print(res.fetchall())
    except sqlite3.Error as e:
        print(e)
else:
    print("Wrong query...")

con.close()
