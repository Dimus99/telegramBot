import sqlite3 as sq
try:
	conn = sq.connect('database.db')
	cursor = conn.cursor()

	cursor.execute("""CREATE TABLE users
		(id text, username text, is_admin text)
		""")
	conn.commit()
	print('Good_users_db')
except:
	print('БД для Users уже создана , для обновления удалите папку database.db и запустите create_db.py')


