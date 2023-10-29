from db_utils import Database
import asyncio

class Main:
	def __init__(self):
		self.db = Database()

	async def print_students(self):
		students = await self.db.get_students()
		result = [i for i in students if len(i[2]) > 10]
		print(f"All students:", *students, sep='\n', end='\n \n')
		print(f"Result:", *result, sep='\n', end='\n \n')

	async def print_genius(self):
		await self.db.update_student()
		students = [i for i in await self.db.get_students() if i[1] == 'Genius']
		print(f"All genius:", *students, sep='\n', end='\n \n')

	async def remove_students(self):
		await self.db.remove_student()
		students = await self.db.get_students()
		print(f"Students successfully cleared:", *students, sep='\n', end='\n \n')

	async def main_function(self):
		await self.db.create_table()
		await self.print_students()
		await self.print_genius()
		await self.remove_students()

if __name__ == "__main__":
	main = Main()
	asyncio.run(main.main_function())