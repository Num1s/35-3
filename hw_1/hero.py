class SuperHero(object):
	people = 'people'
	def __init__(self, name, nickname, superpower, health_points, catchphrase):
		self.name = name
		self.nickname = nickname
		self.superpower = superpower
		self.health_points = health_points
		self.catchphrase = catchphrase

	def __str__(self):
		return f'Nickname: {self.nickname}\n' \
			  f'SuperPower: {self.superpower}\n' \
			  f'HealthPoints: {self.health_points}' \

	def __len__(self):
		return len(self.catchphrase)

	def print_name(self):
		print(f'SuperHero Name: {self.name}')

	def print_health_points(self):
		if isinstance(self.health_points, (int, float)):
			print(f'Health points: {self.health_points * 2} (*2)')
		else:
			print('Error, Health Points can only be int, float')


class AirHero(SuperHero):
	people = 'people'
	def __init__(self, damage, fly = None):
		self.damage = damage
		self.fly = fly

	def 


# Hero = SuperHero('Michael', 'michael_hero', 'Fire', 100.0, 'Fire and Fire!')
# Hero.print_name()
# Hero.print_health_points()
# print(Hero)
# print(len(Hero))