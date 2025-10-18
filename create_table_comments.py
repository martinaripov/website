import sqlite3

connection = sqlite3.connect('sqlite1.db', check_same_thread=False)
cursor = connection.cursor()

# cursor.execute('DROP TABLE IF EXISTS comment;')
# connection.commit()

cursor.execute('''CREATE TABLE comment (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         post_id INTEGER,
         user_id INTEGER,
         content TEXT NOT NULL); ''')

connection.commit()
connection.close()