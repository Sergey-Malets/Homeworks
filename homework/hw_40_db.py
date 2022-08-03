# Создать 2 таблицы в Базе Данных
# Одна будет хранить текстовые данные(1 колонка)
# Другая числовые(1 колонка)
# Есть список, состоящий из чисел и слов.
# Если элемент списка слово, записать его в соответствующую таблицу, затем посчитать длину слова и записать её в числовую таблицу
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел, если нечётное,
# то записать во вторую таблицу слово: «нечётное»
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
# Если меньше, то обновить 1 запись в первой таблице на «hello»

import sqlite3

conn = sqlite3.connect('hw_40_1.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT) ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER) ''')

l = [1208,'qwerty',999, 123435643,'sugar','Hello',6]
for i in l:
    if type(i) is str:
        cursor.execute('''INSERT into tab_1 (col_1) VALUES(?)''',(i,))
        cursor.execute('''INSERT into tab_2 (col_1) VALUES(?)''', (len(i),))
        conn.commit()
    elif type(i) is int:
        if i%2 == 0:
            cursor.execute('''INSERT into tab_2 (col_1) VALUES(?)''', (i,))
            conn.commit()
        else:
            cursor.execute('''INSERT into tab_1 (col_1) VALUES('Нечётное')''')
            conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)
cursor.execute('''SELECT * FROM tab_2''')
k = cursor.fetchall()
print(k)
print(len(k))

if len(k) > 5:
    cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
    conn.commit()
else:
    cursor.execute('''UPDATE tab_1 SET col_1 = "hello" WHERE id = 1''')
    conn.commit()

cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)
cursor.execute('''SELECT * FROM tab_2''')
k = cursor.fetchall()
print(k)

conn.close()

