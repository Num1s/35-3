import aiosqlite

class Database:
	def __init__(self):
		self.name = 'dbs/main.db'

	async def create_table(self):
		async with aiosqlite.connect(self.name) as db:
			cursor = await db.cursor()
			query = '''CREATE TABLE IF NOT EXISTS students (
				id INTEGER,
				name TEXT,
				surname TEXT,
				dob DATE,
				hobby TEXT,
				hw_points INTEGER
			)'''
			await cursor.execute(query)
			await db.commit()

	async def get_students(self):
		async with aiosqlite.connect(self.name) as db:
			cursor = await db.cursor()
			query = 'SELECT * FROM students'
			await cursor.execute(query)
			return await cursor.fetchall()

	async def remove_student(self):
		async with aiosqlite.connect(self.name) as db:
			cursor = await db.cursor()
			query = 'DELETE FROM students WHERE rowid % 2 == 0'
			await cursor.execute(query)
			await db.commit()

	async def update_student(self):
		async with aiosqlite.connect(self.name) as db:
			cursor = await db.cursor()
			query = 'UPDATE students SET name = ? WHERE hw_points > 10'
			await cursor.execute(query, ('Genius',))
			await db.commit()