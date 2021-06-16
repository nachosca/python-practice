import sqlite3

conn = sqlite3.connect("example1.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS EMP(ID INT PRIMARY KEY, NAME TEXT, SALARY REAL)""")
# c.execute("INSERT INTO EMP VALUES (101, 'ABC', 8000)")
# c.execute("INSERT INTO EMP VALUES (102, 'DEF', 8000)")
# c.execute("INSERT INTO EMP VALUES (103, 'GHI', 8000)")
# c.execute("INSERT INTO EMP VALUES (104, 'JKL', 8000)")
# conn.execute("COMMIT")

c.execute(""" SELECT * FROM EMP""")
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# for row in c:
# 	print(row)

# c.execute("UPDATE EMP SET SALARY = 65000 WHERE ID = 102")
# conn.execute("COMMIT")
# c.execute(""" SELECT * FROM EMP where ID = 102""")

# for row in c:
# 	print(row)


c.execute("""DELETE FROM EMP WHERE ID = 103""")

conn.execute("COMMIT")
c.execute(""" SELECT * FROM EMP""")

for row in c:
	print(row)