import sqlite3
from DB_maneger import DB_FILE ,TABLE_NAME



connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE name like "j%"')
cursor.execute(f'UPDATE {TABLE_NAME} SET weight = 67 WHERE id =261')


cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE name like "j%"')

# for row in cursor.fetchall():
#     _id, name, weight = row
#     print(row)



connection.commit()

cursor.close()
connection.close()