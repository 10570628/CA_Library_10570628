import pypyodbc

connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
'Server=20.196.223.198;'
'Database=master;'
'encrypt=yes;'
'TrustServerCertificate=yes;'
'UID=sa;'
'PWD=Pr0gramming!',autocommit = True)

print('hi')

cursor = connection.cursor()
SQLCommand = ("CREATE DATABASE Customer;")
cursor.execute(SQLCommand)
print('done')

connection.close()

connection=connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
'Server=20.196.223.198;'
'Database=Customer;'
'encrypt=yes;'
'TrustServerCertificate=yes;'
'UID=sa;'
'PWD=Pr0gramming!',autocommit = True)

cursor = connection.cursor()
SQLCommand = ("CREATE TABLE test(ID INT);")
cursor.execute(SQLCommand)
SQLCommand = ("INSERT INTO test VALUES(40);")
cursor.execute(SQLCommand)
SQLCommand = ("INSERT INTO test VALUES(42);")
cursor.execute(SQLCommand)
SQLCommand = ("SELECT * FROM test;")
cursor.execute(SQLCommand)
results = cursor.fetchone()
print('First result is:',results[0])
results = cursor.fetchone()
print('Next result is:',results[0])
print('done')

connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
'Server=b751a4c2-4fdf-4ad0-9672-ae980130131c.sqlserver.sequelizer.com;'
'Database=dbb751a4c24fdf4ad09672ae980130131c;'
'encrypt=yes;'
'TrustServerCertificate=yes;'
'UID=znzmwbdlrbzmidhw;'
'PWD=fqFZ7NvwXXhYLk2G5bex3dfooyViiGxhbwhsPiEpkENe3sYDjwFsc2abkrKFZmoq',autocommit = True)

cursor = connection.cursor()
SQLCommand = ("CREATE DATABASE Customer;")
cursor.execute(SQLCommand)
print('done')

connection.close()

cursor = connection.cursor()
SQLCommand = ("CREATE TABLE test(ID INT);")
cursor.execute(SQLCommand)
SQLCommand = ("INSERT INTO test VALUES(40);")
cursor.execute(SQLCommand)
SQLCommand = ("INSERT INTO test VALUES(42);")
cursor.execute(SQLCommand)
SQLCommand = ("SELECT * FROM test;")
cursor.execute(SQLCommand)
results = cursor.fetchone()
print('First result is:',results[0])
results = cursor.fetchone()
print('Next result is:',results[0])
print('done')

