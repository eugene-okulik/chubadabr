import os
import dotenv
import mysql.connector as mysql
import csv

dotenv.load_dotenv()
db = mysql.connect(
    user=os.environ['DB_USER'],
    passwd=os.environ['DB_PASSW'],
    host=os.environ['DB_HOST'],
    port=os.environ['DB_PORT'],
    database=os.environ['DB_NAME']
)
cursor = db.cursor(dictionary=True)
check_query = '''
SELECT
s.`name`,
s.second_name,
g.title 'group_title',
b.title 'book_title',
sub.title 'subject_title',
l.title 'lesson_title',
m.`value` 'mark_value'
FROM
students s
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets sub ON l.subject_id = sub.id
LEFT JOIN "groups" g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
WHERE s.name = %s AND s.second_name = %s AND g.title = %s AND b.title = %s
AND sub.title = %s AND l.title = %s AND m.`value` = %s
'''
file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
csv_path = os.path.join(file_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
with open(csv_path, newline='') as csv_file:
    data = csv.DictReader(csv_file)
    for row in data:
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = (row['name'],
                                                                                               row['second_name'],
                                                                                               row['group_title'],
                                                                                               row['book_title'],
                                                                                               row['subject_title'],
                                                                                               row['lesson_title'],
                                                                                               row['mark_value'])
        cursor.execute(check_query, (name, second_name, group_title, book_title, subject_title, lesson_title,
                                     mark_value))
        db_data = cursor.fetchone()
        if row != db_data:
            print(f'Я не нашёл в БД записи: {row}')

db.close()
