# 1.Сформулируйте SQL запрос для создания таблицы book. Структура таблицы book:
# Поле-Тип - описание
# book_id - INT PRIMARY KEY AUTOINCREMENT
# title - VARCHAR(50)
# author - VARCHAR(30)
# price - DECIMAL(8, 2)
# amount - INT
# 2.Занесите новую строку в таблицуbook
# 3.Выбрать информацию о всех книгах из таблицы book.
import sqlite3

conn = sqlite3.connect('hw_39_db_1.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS book (book_id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(50), author VARCHAR(30), price DECIMAL(8, 2), amount INTEGER)''')

cursor.execute('''INSERT INTO book(title, author, price, amount) VALUES('Атомные привычки', 'Джеймс Клир','29,90', 256)''')
cursor.execute('''INSERT INTO book(title, author, price, amount) VALUES('Граф Монте-Кристо', 'Александр Дюма','59,90', 47)''')
conn.commit()

cursor.execute('''SELECT*FROM book''')
print(cursor.fetchall())