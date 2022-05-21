import sqlite3 as sql

con = sql.connect("autoriza.db")

with open('schema.sql') as f:
    con.executescript(f.read())

cur = con.cursor()

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            ('Aluno', 'PI-II')
            )

con.commit()
con.close()
