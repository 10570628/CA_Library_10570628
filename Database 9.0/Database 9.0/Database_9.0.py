import sqlite3
from Library import Library

conn = sqlite3.connect(':memory:')    ###Refresh database on every test, do not need to delete database to add/remove info - does not retain info if books are removed###

c = conn.cursor()
###CREATE TABLE####
c.execute("""CREATE TABLE library (
            first text,
            middle text,
            last text
            )""")

                             ###INSERT BOOK###
def insert_bok(bok):
    with conn:
        c.execute("INSERT INTO library VALUES (:first, :middle, :last)", {'first': bok.first, 'middle': bok.middle, 'last': bok.last})

                             ###FIND BOOK### #(first name = title, Middle name = author, last = date book was published)#
def get_bok_by_name(middlename):
    c.execute("SELECT * FROM library WHERE middle=:middle", {'middle': middlename})

    return c.fetchall()

def update_last(bok, last):  ###Update book info###
    with conn:
        c.execute("""UPDATE library SET last = :last
                    WHERE first = :first AND middle = :middle""",
                  {'first': bok.first, 'middle': bok.middle, 'last': last})


def remove_emp(bok):        ###remove book###
    with conn:
        c.execute("DELETE from library WHERE first = :first AND middle = :middle",
                  {'first': bok.first, 'middle': bok.middle})

                           ###Books to add to database - 8 in total###

bok_1 = Library('Dracula','Bram Stoker', '26/05/1897')
bok_2 = Library('Dune', 'Frank Herbert', '01/08/1865')
bok_3 = Library('The Hobbit', 'J. R. R. Tolkien', '21/09/1937')
bok_4 = Library('The Lord of the Rings, the Fellowship of the Ring', 'J. R. R. Tolkien', '29/07/1954')
bok_5 = Library('The Lord of the Rings, the Two Towers', 'J. R. R. Tolkien', '11/11/1954')
bok_6 = Library('The Lord of the Rings, the Return of the King', 'J. R. R. Tolkien', '20/10/1955')
bok_7 = Library('Storm Front', 'Jim Butcher', '01/04/2000')
bok_8 = Library('Fool Moon', 'Jim Butcher', '09/01/2001')

insert_bok(bok_1)
insert_bok(bok_2)
insert_bok(bok_3)
insert_bok(bok_4)
insert_bok(bok_5)
insert_bok(bok_6)
insert_bok(bok_7)
insert_bok(bok_8)


#to remove book - coded out to not remove something by default#
#remove_emp(bok_1)

                    ###to find a book - it's set to by author (Middle) 

boks = get_bok_by_name('Jim Butcher')
print(boks)
conn.commit()
conn.close()
