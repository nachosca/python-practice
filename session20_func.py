# - code reuse
# - modularity


# s = "Python,HTML,CSS"
# print(s.index("HTML"))

# func call
# fun def



def value_reverses(value):
	if type(value)==list or type(value)==str:
		reverse = value[::-1]
	else:
		temp = str(value)
		reverse = temp[::-1]
	return reverse

s = "Python"
result = value_reverses(s)
print(result)


# l = [10,20,30,40]
# l.append(50)
# print(l)

l = [100,200,300,400]
result = value_reverses(l)
print(l)

num = 100
result = value_reverses(100)
print(result)