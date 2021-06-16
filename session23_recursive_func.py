
# factorial(5) = 5 * factorial(4)
# 							4 * factorial(3)
# 										3 * factorial(2)
# 											2 * factorial(1)
# 														1


# def factorial(num):
# 	if num == 1:
# 		return 1
# 	else:
# 		return num * factorial(num-1)


# num1 = 400
# result = factorial(num1)
# print(result)


l = [100,200,300,400,500,600,700,800,900]
key = 300

def binary_search(l,key):
	if len(l) == 0:
		return False
	else:
		mid = len(l) // 2
		if l[mid] == key:
			return True
		elif key < l[mid]:
			return binary_search(l[:mid],key)
		else:
			return binary_search(l[mid+1:], key)


result = binary_search(l,key)
print(result);

# mid = 9/2 = 4 = 500 == 700 ? false


# [600,700,800,900]

# mid = 4/2 =2 

# 800 == 700? false

# [600, 700]
# mid == 2/2 = 1

# 700==700 return true;