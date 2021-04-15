import sqlite3

db = sqlite3.connect('books.db')

cur = db.cursor()

cur.execute('SELECT * FROM books ORDER BY title')

for x in cur.fetchall():
    print(x)


cur.execute('SELECT * FROM books WHERE price > 10')

print('*' * 20)
for x in cur.fetchall():
    print(x)

cur.execute('SELECT author FROM books')
print(cur.fetchall())

db.close()
