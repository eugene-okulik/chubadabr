import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO students (name, second_name) VALUES('Henri', 'Morgan')")
student_id = cursor.lastrowid
print('student_id:', student_id)
db.commit()
insert_books = "INSERT INTO books(title, taken_by_student_id) VALUES(%s, %s)"
cursor.executemany(insert_books, [('Tales from the Yawning portal_1', student_id),
                                  ('Маус_1', student_id),
                                  ('Задача трёх тел_1', student_id)])
db.commit()
cursor.execute("INSERT INTO `groups`(title, start_date, end_date) VALUES('Secret group_1', 'Mar 8 2024', 'TBA')")
group_id = cursor.lastrowid
print('group_id:', group_id)
db.commit()
cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")
db.commit()
cursor.execute("INSERT INTO subjets(title) VALUES('Sorcery_1')")
subject_1 = cursor.lastrowid
db.commit()
cursor.execute("INSERT INTO subjets(title) VALUES('Potionmaking_1')")
subject_2 = cursor.lastrowid
db.commit()
insert_lesson = "INSERT INTO lessons(title, subject_id) VALUES(%s, %s)"
cursor.execute(insert_lesson, ('Origins of sorcery_1', subject_1))
lesson_1 = cursor.lastrowid
print('lesson_1:', lesson_1)
cursor.execute(insert_lesson, ('Advanced sorcery_1', subject_1))
lesson_2 = cursor.lastrowid
print('lesson_2:', lesson_2)
cursor.execute(insert_lesson, ('Lotions and potions_1', subject_2))
lesson_3 = cursor.lastrowid
print('lesson_3:', lesson_3)
cursor.execute(insert_lesson, ('Potionmaking accessories_1', subject_2))
lesson_4 = cursor.lastrowid
print('lesson_4:', lesson_4)
db.commit()
cursor.executemany(
    "INSERT INTO marks(`value`, lesson_id, student_id) VALUES(%s, %s, %s)",
    [('B-', lesson_1, student_id), ('A+', lesson_2, student_id),
     ('C', lesson_3, student_id), ('C+', lesson_4, student_id)])
db.commit()
cursor.execute(f"SELECT * FROM marks WHERE student_id = {student_id}")
marks = cursor.fetchall()
print('marks:', marks)
cursor.execute(f"SELECT * FROM books WHERE taken_by_student_id = {student_id}")
books = cursor.fetchall()
print('books:', books)
all_for_student_query = f'''SELECT
s.`name`,
s.second_name,
g.title 'Группа',
b.title 'Borrowed book',
sub.title 'Предмет',
l.title 'Урок',
m.`value` 'Оценка'
FROM
students s
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets sub ON l.subject_id = sub.id
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
WHERE s.id = {student_id}
'''
cursor.execute(all_for_student_query)
all_for_student_data = cursor.fetchall()
print('all_for_student_data:', all_for_student_data)
db.close()
