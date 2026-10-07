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

print("------------------")

Items={
    ("Banglore",800),
    ("Kolkata",200),
    ("Bhopal",100)
}

cur.executemany("insert into t values (?,?)",Items)
con.commit()

sel = "SELECT * FROM t"
cur.execute(sel)
print(cur.fetchall())