import sqlite3

conn = sqlite3.connect('library.db')

c = conn.cursor()

#########CREATE DATABASE~~~~~~
# c.execute("""CREATE TABLE library (
#            first text,
#           middle text,
#            last text
#            )""")



###########INSERT###############
#c.execute("INSERT INTO library VALUES ('Dune', 'Frank Herbert', '01/08/1865')")


###########SEARCH############
c.execute("SELECT * FROM library WHERE middle = 'Jim Butcher'")


#########SHOW DATABASE########
#print(c.fetchone())
print(c.fetchall())


conn.commit()

conn.close()
