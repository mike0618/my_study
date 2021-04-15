import sqlite3
import pandas as pd

db = sqlite3.connect('books.db')

# read data from SQL to pandas dataframe.
data = pd.read_sql_query('Select * from books;', db)

# show top 5 rows
# print(data.head())

# print(data)
#
new_row = {'id': '12', 'author': 'P. G. Wodehouse', 'title': 'Luck of the Bodkins', 'price': 6.49}

data = data.append(new_row, ignore_index=True)

print(data)

data.to_sql('books', db, if_exists='replace', index = False)
