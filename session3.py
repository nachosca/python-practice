#Datatypes:
#Int: 

num1 = 100
print(type(num1))


#Float

num2 = 15.25
print(type(num2))


num3 = 150
print(id(num3))
num3 = 155
print(id(num3))


print()
s1 = "Python"
print(id(s1))
print(s1, type(s1))

s1 = "new value"
print(id(s1))

print()
s2 = "'Python' sample string"
print(id(s2))
print(s2, type(s2))


#Lists: []

print()
l = [10, 20, 30, 40, 50, "Python", "Django"]
print(l)
print((id(l)))
l.append(60)
print(l)
print((id(l)))


#Tuples:
print()

t = (10, 20, 30)
print(t)

#6 dictionary:
print()
d = {"name": "ABC", "email":"asd@asd.com"}

print(d)

#Set {}
print()
s = {10, 20, 30, 40}

print(s)

# boolean:


# complex: 3 + 3j


print()
help(str)