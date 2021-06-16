# - position argument
# - default argument
# - keyword



# def linear_search(l,key):
# 	for x in l:
# 		if key==x:
# 			return True
# 	else:
# 		return False


# l = [100,200,300,400,500]
# key = 400
# result = linear_search(l,key)
# print(result)



# 8 char
# 1 Upper
# 1 lower
# 1 special
# 5 digits

# ord
# chr

# print(ord('a'),ord('z'))
# print(ord('A'),ord('Z'))


# import random
# def gen_password(length=8):
# 	l = ['@','#','$','&']

# 	upper = chr(random.randint(65,90))
# 	lower = chr(random.randint(97,122))
# 	special = random.choice(l)
# 	digits = random.randint(10000,99999)
# 	password = upper + lower + special + str(digits)
# 	l = random.sample(password,length)
# 	password = ("").join(l)
# 	return password


# result = gen_password()
# print(result)

# def validate(user,passw):
# 	if user == 'ABC' and passw == "Abc@123":
# 		print("Valid Password")
# 	else:
# 		print("Invalid Password")


# validate("abc123","Abc@123")
# validate("ABC","Abc@123")
# validate(passw="Abc@123",user="ABC")


help(print)

print(100,200,sep=",",end=" ")
print("Hi")