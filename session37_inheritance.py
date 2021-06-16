class Account:
	count = 0

	@classmethod
	def incr_count(cls):
		cls.count += 1

	@classmethod
	def get_count(cls):
		return cls.count

	@staticmethod
	def print_val():
		print("Static method in account class")

	def __init__(self, cust_id, name, initial_balance=0):
		self.__id = cust_id
		self.__name = name
		self.__balance = initial_balance
		Account.incr_count()

	def get_id(self):
		return self.__id

	def get_name(self):
		return self.__name

	def get_balance(self):
		return self.__balance

	def deposit(self, amount):
		self.__balance += amount
		return self.__balance

	def withdraw(self, amount):
		if amount > self.__balance:
			return "Insufficient balance"
		self.__balance -= amount
		return self.__balance


	"""docstring for ClassName"""
class Saving_Account(Account):
	def __init__(self,id,name,initial_balance=0):
		super().__init__(id,name,initial_balance)
		self.limit = 50000

	def withdraw(self,amount):
		if amount < self.limit:
			new_bal = super().withdraw(amount)
			self.limit -= amount
			return new_bal
		else:
			print("Daily limit reached")

# cust1 = Saving_Account(101,"ABC")
# print(cust1.__dict__)

# print(cust1.deposit(60000))
# print(cust1.withdraw(40000))
# print(cust1.withdraw(40000))

# tengo clase A y B, y puede heredar de C

class A:
	pass

class B:
	pass
	
class C(B,A):
	pass

obj = C()
help(obj)
		