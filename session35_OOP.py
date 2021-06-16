
# cust id
# name
# balance


# deposit
# withdraw



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
class Saving_account(Account):
	pass
		

customer1 = Account("101","ABC")

# print(customer1.__dict__)
# print(customer1._Account__id)
# print(customer1)

customer2 = Account("102","XYZ")
# print(customer1)

customer3 = Account("103","PQR")
# print(customer1)
customer4 = Account("104","QWE")


# print(customer1.id, customer1.name, customer1.balance)
# print(customer1.get_balance())
# print(customer1.deposit(5000))
# print(customer1.withdraw(7000))

customer2.deposit(2000)
customer3.deposit(3000)
customer4.deposit(4000)


# l = [customer1,customer2,customer3,customer4]

# for x in l:
# 	if x.get_balance() < 4000:
# 		print(x.get_id(), x.get_name())
# 		

# print(Account.count)

# print(customer1.count)
# print(customer2.count)
# print(customer3.count)

# # Account.count += 5


# print(customer1.count)
# print(customer2.count)
# print(customer3.count)

# print(Account.__dict__)
# print(customer1.__dict__)

# print(Account.__dict__)
# print(customer1.__dict__)

# customer1.count = 100

# print(customer1.__dict__)

# print(customer1.count)
# print(customer2.count)
# print(customer3.count)

# print(Account.get_count())
# print(customer1.get_count())


Account.print_val()