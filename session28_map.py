# map
# filter
# lambda


# def sqr(num):
# 	return num**2

# l = [10,20,30,40,50,60]

# l2=list(map(sqr,l))

# print(l2)

# def add(num1, num2):
# 	return num1+num2


# l1 = [100,200,300,400,500]
# l2 = [10,20,30,40,50]

# result = list(map(add,l1,l2))

# print(result)


# l = [100,115,120,125,130,140]
	

# def check_num(num):
# 	return num % 2 == 0

# result = list(filter(check_num,l))
# print(result)


# lambda


# l = [10,20,30,40,50,60]

# result = list(map(lambda num1:num1**2, l))
# print(result)


# l = [100,115,120,125,130,140]

# result = list(filter(lambda num:num%2==0,l))
# print(result)


d = {1:50,2:40,3:30,4:20,5:10}

l = sorted(d.items(),key=lambda x:x[1])
# l = sorted(d.items(),reverse=True)
print(l)

# help(sorted)