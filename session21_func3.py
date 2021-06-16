# variable length position argument
# - variable length keyword args


# l = [100,200,300,400]
# l.append(500)
# print(l)


# def add_value(*args):
# 	l=[]
# 	for x in args:
# 		l.append(x)
# 	return l

# result = add_value(100,200,300,400,500)
# print(result)
# result = add_value(100,200)
# print(result)
# result = add_value(100,200,300,400,500,600,700,800)
# print(result)





# name,email,contact,dob

def get_details(**kwargs):
	print(kwargs)


get_details(name="ABC",email="abc@gmail.com",contact=12341234,dab = "01-01-1945")
get_details(name="ABC",email="abc@gmail.com",dab = "01-01-1945")
get_details(name="ABC",contact=12341234,dab = "01-01-1945")


