import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()

sql = "CREATE TABLE t(city, amt)"
cur.execute(sql)

q = "INSERT INTO t VALUES (?, ?)"
cur.execute(q, ("Delhi", 500))
cur.execute(q, ("Mumbai", 800))

sel = "SELECT * FROM t"
for row in cur.execute(sel):
    print(row[0],"-",row[1])