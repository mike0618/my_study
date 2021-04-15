# to work with sqlite we need to import sqlite3 from standard library
import sqlite3

db = sqlite3.connect('books.db')

cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS books(
    id integer PRIMARY KEY,
    title text NOT NULL,
    author text NOT NULL,
    price real);''')

# go to https://sqlitebrowser.org/
# https://docs.python.org/3/library/sqlite3.html

cur.execute('''INSERT INTO books(id, title, author, price)
        VALUES('1', 'Untold Stories', 'Alan Bennett', '17,49')''')

book_list = [('2', 'Lucky Jim', 'Kingsley Amis', '4.99'),
             ('3', 'Animal Farm', 'George Orwell', '7.49'),
             ('4', 'Why I am so Clever', 'Friedrich Nietzsche', '12.49'),
             ('5', 'AI and the Problem of Control', 'Stuart Russel', '21.49'),
             ('6', 'Being Human in the Age of AI', 'Max Tegmark', '9.99'),
             ('7', 'Paths, Dangers, Strategies', 'Nick Bostrom', '8.49'),
             ]
cur.executemany('''INSERT INTO books(id, title, author, price)
        VALUES(?,?,?,?)''', book_list)

cur.execute('SELECT * FROM books')
print(cur.fetchall())

db.commit()
db.close()
