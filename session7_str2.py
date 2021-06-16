# help(str)
# print(dir(str))

# format

# num1=100
# num2=200
# print("Value of num1 is",num1,"Value of num2",num2)
# print("Value of num1 is {}, Value of num2 {}".format(num1, num2))
# print("Value of num2 is {1}, Value of num1 {0}".format(num1, num2))
# print("Value of num1 is {val2}, Value of num2 {val1}".format(val2=num1, val1=num2))



# s = "python sample string"
# s1 = s.capitalize()
# print(s)
# print(s1)

# s = "python sample string"
# # print(id(s))
# s = s.capitalize()
# s= s.title()
# print(s.istitle())
# # print(s)
# # print(id(s))

# # upper
# # lower
# # title

# print(s.upper())
# print(s.lower())
# print(s.title())


# isupper
# islower
# istitle

# iscapitalize no existe


#split
#join

# s = "HTML,CSS,PYTHON,JAVA,Django"
# l = s.split(",")
# print(l)

# s1 = (" ").join(l)
# print(s1)

# s1 = "abcd"
# s2 = "1234"

# s3 = "Python Sample string abcd"

# # maketrans
# # translate

# table = str.maketrans(s1, s2)
# result = s3.translate(table)
# print(result)




# index
# find
# rfind function

# s = "HTML,CSS,PYTHON,PYTHON,PYTHON"
# print("PYTHON" in s)
# # print(s.index("PYTHON"))

# print(s.rfind("PYTHON"))


# s = "****This is a sample string*****"
# s1 = s.rstrip("*")
# s2 = s.lstrip("*")
# s3 = s.strip("*")
# print(s1)
# print(s2)
# print(s3)


# s = "python"

# s1 = s.center(20,"*")
# s2 = s.ljust(20,"*")
# s3 = s.rjust(20,"*")

# print(s1)
# print(s2)
# print(s3)


# s = "html,css,python,html"

# s1 = s.replace("html", "HTML5")
# print(s1)


help(str)
print(dir(str))


