# list

# - lists are mutable - add update delete
# - ordered, indexing and slicing
# - heterogeneous datatype



# l = [10, 20, 30 , 40, "Python", "Java", [100,200,300]]
# print(l, type(l))

# indexing and slicing:

# print(l[0])
# print(l[20])

# print(l[::-1])


# l = [100,200,300,400,500]

# for x in l[::2]:
# 	print(x)

# append
# num1 = 100
# print(id(num1))
# # print(id(l))
# l.append(600)
# print(l)
# print(id(l[0]))


# l.extend("Python")
# print(l)

# l.extend([500,600,700,800])
# print(l)

# l.insert(1, 1000)
# print(l)



l = [10, 20, 30]
l2 = l.copy()
l.append(40)
print(l,l2)
print(id(l))
print(id(l2))