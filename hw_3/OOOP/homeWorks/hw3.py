
class Bank(object):
	def __init__(self, name, balance):
		self._name = name
		self._balance = balance

	def moneyX(self):
		money = int(input('Enter a money amount: '))
		self._balance += money
		print('Success!', self._balance)

	def _kill(self):
		self._balance = 0
		print('Success!', self._balance)

	def __jackpot(self):
		self._balance *= 10
		print('Success!', self._balance)

	def _copy_money(self, other_account):
		self._balance += other_account._balance
		print('Success!', self._balance)