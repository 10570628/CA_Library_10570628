import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE library (
            first text,
            middle text,
            last text
            )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO library VALUES (:first, :middle, :last)", {'first': bok.first, 'middle': bok.middle, 'last': bok.last})


def get_bok_by_name(lastname):
    c.execute("SELECT * FROM library WHERE middle=:middle", {'middle': middlename})
    return c.fetchall()


def update_pay(bok, last):
    with conn:
        c.execute("""UPDATE library SET last = :last
                    WHERE first = :first AND middle = :middle""",
                  {'first': bok.first, 'middle': bok.middle, 'last': last})


def remove_emp(bok):
    with conn:
        c.execute("DELETE from library WHERE first = :first AND middle = :middle",
                  {'first': bok.first, 'middle': bok.middle})

bok_1 = Book('Dracula', 'Bram Stoker', '26/05/1897')
bok_2 = Book('Dune', 'Frank Herbert', '01/08/1865')

insert_bok(bok_1)
insert_bok(bok_2)

boks = get_boks_by_name('Frank Herbert')
print(emps)


remove_emp(emp_1)

boks = get_emps_by_name('Bram Stoker')
print(emps)
#conn.commit()
conn.close()