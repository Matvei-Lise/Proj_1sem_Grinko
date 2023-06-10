import sqlite3 as sq

#  СОЗДАНИЕ БАЗЫ
# with sq.connect('library.db') as con:
#   cur = con.cursor()

# cur.execute ("""CREATE TABLE IF NOT EXISTS author(
#   author_id INTEGER PRIMARY KEY,
#   surname VARCHAR NOT NULL,
#   name VARCHAR NOT NULL
#   )""")

# cur.execute ("""CREATE TABLE IF NOT EXISTS book(
#   book_id INTEGER PRIMARY KEY,
#   title VARCHAR NOT NULL,
#   chapter VARCHAR NOT NULL,
#   pub_house VARCHAR NOT NULL,
#   pub_date DATE NOT NULL,
#   stor_loc VARCHAR NOT NULL,
#   FOREIGN KEY (chapter) REFERENCES chapters(chapter) ON DELETE CASCADE ON UPDATE CASCADE,
#   FOREIGN KEY (pub_house) REFERENCES pub_houses(pub_house) ON DELETE CASCADE ON UPDATE CASCADE
#   )""")

# cur.execute ("""CREATE TABLE IF NOT EXISTS chapters(
#     id_chapter INT auto_increment PRIMAY KEY NOT NULL,
#     chapter VARCHAR UNIQUE
# )""")

# cur.execute ("""CREATE TABLE IF NOT EXISTS pub_houses(
#   pub_house_id auto_increment PRIMAY KEY NOT NULL,
#   pub_house VARCHAR UNIQUE,
#   city VARCHAR NOT NULL
#   )""")

# cur.execute ("""CREATE TABLE IF NOT EXISTS author_book(
#   author_book_id INTEGER PRIMARY KEY ,
#   book_id INTEGER NOT NULL,
#   author_id INTEGER NOT NULL,
#   FOREIGN KEY (book_id) REFERENCES book(book_id),
#   FOREIGN KEY (author_id) REFERENCES author(author_id)
#   )""")

# ЗАПОЛНЕНИЕ ДАННЫМИ

# info_author = [
#     (1,'Иванов','Александр'),
#     (2, 'Петров', 'Александр'),
#     (3, 'Петров', 'Иван'),
#     (4, 'Фёд', 'Лидия'),
#     (5, 'Сава', 'Анна'),
#     (6, 'Ларе', 'Валерия'),
#     (7, 'Дизне', 'Никита'),
#     (8, 'Аарин', 'Генадий'),
#     (9, 'Лысенко', 'Ирина'),
#     (10, 'Ковров', 'Николай')
# ]
# with sq.connect('library.db') as con:
#     cur = con.cursor()
#     cur.executemany('INSERT INTO author VALUES (?,?,?)', info_author)

# info_book = [
#     (1, 'Грустный подсолнух', 'Фентези', 'Леон', '1999', 'Библиотека №1'),
#     (2, 'Красное яблоко', 'Класика', 'Круз', '2022', 'Библиотека №1'),
#     (3, 'Две вишенки', 'Ужасы', 'Девиль', '1981', 'Библиотека №2'),
#     (4, 'Старый арахис', 'Фантастика', 'Леон', '2005', 'Склад'),
#     (5, 'Война кобачков', 'Роман', 'Штиль', '2001', 'Настенная полка'),
#     (6, 'Злобный лук', 'Роман', 'Кондо', '2007', 'Шкаф у стены'),
#     (7, 'Солёная соль', 'Детектив', 'Кондо', '2003', 'Настенная полка'),
#     (8, 'Сладкий уксус', 'Фентези', 'Ариель', '2023', 'Полка'),
#     (9, 'Синее море', 'Фентези', 'Леон', '2019', 'Шкаф у стены'),
#     (10, 'Бушуют бураны', 'Ужасы', 'Кан-Кан', '2015', 'Полка')
# ]
# with sq.connect('library.db') as con:
#     cur = con.cursor()
#     cur.executemany('INSERT INTO book VALUES (?,?,?,?,?,?)', info_book)

# info_chapters = [
#     ('1', 'Фентези'),
#     ('2', 'Ужасы'),
#     ('3', 'Класика'),
#     ('4', 'Детектив'),
#     ('5', 'Фантастика'),
#     ('6', 'Роман')
# ]
# with sq.connect('library.db') as con:
#     cur = con.cursor()
#     cur.executemany('INSERT INTO chapters VALUES (?,?)', info_chapters)

# info_pub_houses = [
#     ('1','Леон', 'Москва'),
#     ('2','Кан-Кан', 'Ростов-на-дону'),
#     ('3','Ариель', 'Санкт-Петербург'),
#     ('4','Кондо', 'Санкт-Петербург'),
#     ('5','Штиль', 'Краснодар'),
#     ('6','Круз', 'Москва'),
#     ('7','Девиль', 'Кропоткин'),
#     ('8','OReilly Media', 'Москва')
# ]
# with sq.connect('library.db') as con:
#     cur = con.cursor()
#     cur.executemany('INSERT INTO pub_houses VALUES (?,?,?)', info_pub_houses)

# info_author_book = [
#     (1, 1, 1),
#     (2, 2, 2),
#     (3, 3, 3),
#     (4, 4, 4),
#     (5, 5, 5),
#     (6, 6, 6),
#     (7, 7, 7),
#     (8, 8, 8),
#     (9, 9, 9),
#     (10, 10, 10)
# ]
# with sq.connect('library.db') as con:
#     cur = con.cursor()
#     cur.executemany('INSERT INTO author_book VALUES (?,?,?)', info_author_book)

# with sq.connect('library.db') as con:
#     cur = con.cursor()
# Выборка

# cur.execute('SELECT * FROM book ORDER BY pub_date DESC') # 1
# cur.execute('SELECT * FROM book WHERE book_id = (SELECT book_id FROM author_book where author_id = 1)') # 2
# cur.execute('SELECT * FROM book WHERE chapter = "Ужасы"') # 3
# cur.execute('SELECT * FROM book WHERE pub_house = "Круз"') # 4
# cur.execute('SELECT * FROM author ORDER BY name') # 5
# cur.execute('SELECT * FROM book WHERE title = "Старый арахис" and pub_date = "2005"') # 6
# cur.execute('SELECT * FROM book WHERE book_id = (SELECT book_id FROM author_book where author_id = 4) and pub_date ORDER BY pub_date DESC') # 7
# cur.execute('SELECT * FROM book WHERE pub_date = "1999"') # 8
# cur.execute('SELECT * FROM author WHERE author_id = (SELECT author_id FROM author_book where book_id = (SELECT book_id FROM book where pub_house = "Девиль"))') # 9
# cur.execute('SELECT * FROM book WHERE title LIKE "%яблоко%"') # 10

# res = cur.fetchall()
# print(res)

# with sq.connect('library.db') as con:
#     cur = con.cursor()
# # Обновление
# # 1. Обновить год издания всех книг, написанных автором с фамилией "Иванов", установив год издания равным 2022:
#     cur.execute("""UPDATE book SET pub_date = "2022" WHERE book_id IN (SELECT book_id FROM author_book JOIN author ON author_book.author_id = author.author_id WHERE surname = 'Иванов')""")
# # 2. Обновить название и год издания книги, хранящейся в городе "Москва", установив название "Новая книга" и год издания равным 2023:
#     cur.execute("UPDATE book SET title = 'Новая книга', pub_date = 2023 WHERE pub_house IN (SELECT pub_house FROM pub_houses WHERE city = 'Москва')")
# # 3. Обновить название и раздел всех книг, написанных автором с именем "Александр" и фамилией "Петров", установив название "Новое название" и раздел "Фантастика":
#     cur.execute("""UPDATE book SET title = 'Новое название', chapter = (SELECT chapter FROM chapters WHERE chapter = 'Фантастика') WHERE book_id IN (SELECT book_id FROM author_book JOIN author ON author_book.author_id = author.author_id WHERE name = 'Александр' AND surname = 'Петров')""")
# # 4. Обновить название всех книг, которые были опубликованы в годы с 2010 по 2015 включительно, установив название "Старое название":
#     cur.execute("UPDATE book SET title = 'Старое название' WHERE pub_date BETWEEN 2010 AND 2015")
# # 5. Обновить место хранения всех книг, написанных автором с кодом 7, установив место хранения "Библиотека №2":
#     cur.execute("""UPDATE book SET stor_loc = 'Библиотека №2' WHERE book_id IN (SELECT book_id FROM author_book WHERE author_id = 7)""")
# # 6. Обновление города из таблицы Издательства по коду города в таблице Книги:
#     cur.execute("""UPDATE pub_houses SET city = (SELECT city FROM book WHERE book.pub_house = pub_houses.pub_house)""")
# # 7. Обновление кода автора в таблице АвторКниги по коду автора в таблице Авторы:
#     cur.execute("""UPDATE author_book SET author_id = (SELECT author_id FROM author WHERE author.author_id = author_book.author_id)""")
# # 8. Обновление названия раздела в таблице Книги по названию раздела в таблице Разделы:
#     cur.execute("""UPDATE book SET chapter = (SELECT chapter FROM chapters WHERE chapters.chapter = book.chapter)""")
# # 9. Обновление года издания в таблице book по году издания в таблице author_book:
#     cur.execute("""UPDATE book SET pub_date = '2022' WHERE book_id IN (SELECT book_id FROM author_book WHERE pub_date = 2021)""")
# # 10. Обновление места хранения в таблице book по названию издательства в таблице pub_houses:
#     cur.execute("""UPDATE book SET stor_loc = 'Книжный шкаф 3' WHERE pub_house IN (SELECT pub_house FROM pub_houses WHERE pub_house = 'Штиль')""")
# # 11. Обновление фамилии автора в таблице authors по коду автора в таблице author_book:
#     cur.execute("""UPDATE author SET surname = 'Новая фамилия' WHERE author_id IN (SELECT author_id FROM author_book WHERE author_id = 1)""")
# # 12. Обновить год издания всех книг, изданных в городе "Москва", на 2022 год.
#     cur.execute("""UPDATE book SET pub_date = '2022' WHERE pub_house IN (SELECT pub_house FROM pub_houses WHERE city = 'Москва')""")
# # 13. Обновить место хранения всех книг, написанных автором с фамилией "Иванов", на "Книжный шкаф 1".
#     cur.execute("""UPDATE book SET stor_loc = 'Книжный шкаф 1' WHERE book_id IN (SELECT book_id FROM author_book WHERE author_id IN (SELECT author_id FROM author WHERE surname = 'Иванов'))""")
# # 14. Обновить год издания всех книг, написанных автором с именем "Анна", на 2023 год.
#     cur.execute("""UPDATE book SET pub_date = '2023' WHERE book_id IN (SELECT book_id FROM author_book WHERE author_id IN (SELECT author_id FROM author WHERE name = 'Анна'))""")
# # 15. Обновить название раздела всех книг, изданных в городе "Санкт-Петербург", на "Классика"
#     cur.execute("""UPDATE book SET chapter = 'Классика' WHERE pub_house IN (SELECT pub_house FROM pub_houses WHERE city = 'Санкт-Петербург')""")
# # 16. Обновить год издания всех книг, написанных автором с фамилией "Петров", на 2024 год.
#     cur.execute("""UPDATE book SET pub_date = '2024' WHERE book_id IN (SELECT book_id FROM author_book WHERE author_id IN (SELECT author_id FROM author WHERE surname = 'Петров'))""")
#
# # Удаление
# with sq.connect('library.db') as con:
#     cur = con.cursor()

# # 1. Удалить все записи из таблицы Книги, у которых Раздел = 'Фантастика':
# cur.execute("DELETE FROM book WHERE chapter = 'Фантастика'")
#
# # 2. Удалить все записи из таблицы Книги, у которых ГодИздания меньше 2000:
# cur.execute("DELETE FROM book WHERE pub_date < 2000")
#
# # 3. Удалить все записи из таблицы АвторКниги, у которых КодАвтора равен 1:
# cur.execute("DELETE FROM author_book WHERE author_id = 1")
#
# # 4. Удалить все записи из таблицы Авторы, у которых Фамилия начинается с буквы "А":
# cur.execute("DELETE FROM author WHERE surname LIKE 'А%'")
#
# # 5. Удалить все записи из таблицы Издательства, у которых Город равен "Москва":
# cur.execute("DELETE FROM pub_houses WHERE city = 'Москва'")
#
# # 6. Удалить все записи из таблицы АвторКниги, у которых КодКниги равен 10:
# cur.execute("DELETE FROM author_book WHERE book_id = 10")
#
# # 7. Удалить все записи из таблицы Книги, у которых МестоХранения равно "Склад":
# cur.execute("DELETE FROM book WHERE stor_loc = 'Склад'")
#
# # 8. Удалить все записи из таблицы Разделы, у которых Раздел равен "Детектив":
# cur.execute("DELETE FROM chapters WHERE chapter = 'Детектив'")
#
# # 9. Удалить все записи из таблицы АвторКниги, у которых КодАвтора равен 2:
# cur.execute("DELETE FROM author_book WHERE author_id = 2")
#
# # 10. Удалить все записи из таблицы Издательства, у которых Издательство равно "OReilly Media":
# cur.execute("DELETE FROM pub_houses WHERE pub_house = 'OReilly Media'")
#
# # 11. Удалить все записи из таблицы Книги, у которых Название содержит слово "Война":
# cur.execute("DELETE FROM book WHERE title LIKE '%Война%'")
#
# # 12. Удалить все книги, которые были изданы до 2000 года включительно и хранятся в "Библиотека №1".
# cur.execute("DELETE FROM book WHERE pub_date <= 2000 AND stor_loc = 'Библиотека №1'")
#
# # 13. Удалить всех авторов, у которых нет книг в таблице Книги.
# cur.execute("DELETE FROM author WHERE author_id NOT IN (SELECT DISTINCT author_id FROM author_book)")
#
# # 14. Удалить все книги, изданные в городе "Москва", из таблицы "Книги".
# cur.execute("DELETE FROM book WHERE pub_house IN (SELECT pub_house FROM pub_houses WHERE city = 'Москва')")
#
# # 15. Удалить всех авторов, чьи фамилии начинаются на букву "А" из таблицы "authors" и соответствующие записи из таблицы "author_book".
# cur.execute("DELETE FROM author WHERE surname LIKE 'А%' AND author_id IN (SELECT author_id FROM author_book)")
# cur.execute("DELETE FROM author_book WHERE author_id IN (SELECT author_id FROM author WHERE surname LIKE 'А%')")
#
# # 16. Удалить все записи из таблицы "author_book", связанные с книгами, изданными в городе "Москва".
# cur.execute("""DELETE FROM author_book WHERE book_id IN (SELECT book_id FROM book WHERE pub_house IN (SELECT pub_house FROM pub_houses WHERE city = 'Москва'))""")
#
# # 17. Удалить все книги из таблицы "book", которые были написаны авторами с фамилиями, начинающимися на букву "П"
# cur.execute("""DELETE FROM book WHERE book_id IN (SELECT book_id FROM author_book WHERE author_id IN (SELECT author_id FROM author WHERE surname LIKE 'П%'))""")
#
# # 18. Удалить все книги из таблицы "book", которые были изданы в городах с названиями, начинающимися на букву "Н"
# cur.execute("DELETE FROM book WHERE pub_house IN (SELECT pub_house FROM pub_houses WHERE city LIKE 'Н%')")
#
# # 19. Удалить все записи из таблицы "author_book", связанные с книгами, изданными в городах, название которых начинается на букву "Н"
# cur.execute("""DELETE FROM author_book WHERE book_id IN ( SELECT book_id FROM book JOIN pub_houses ON book.pub_house = pub_houses.pub_house WHERE pub_houses.city LIKE 'Н%')""")