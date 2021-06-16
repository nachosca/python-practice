import re

# - any char
# [a-zA-Z] - chars class a or b or c ... or z or A or B or ... Z
# [0-9] - digit class 0 or 1 or 2 or ... 9

# + - at least one occurence [a-z]+
# * - zero or more [a-z]*


# ^ - start of string
# $ - end of string 

# ? - optional

# [a-z]{4} - 4 occurrences of chars
# [a-z]{2-4} - 2 to 4 occurrences of chars




# 5 chars, 4 digits, 1 char
# s = "ABCDE1234A"
# r = re.compile("[A-Z]{5}[0-9]{4}[A-Z]")
# s = "AAAAABCDE1234AAAA"
# r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")
# si enmcuentra la regex devuelve el string, sino vacío
# l = re.findall(r,s) 
# print(l)


# s = "888123456789"
# r = re.compile("^[6-9][0-9]{9}$")
# l = re.findall(r,s)
# print(l)


# dd-mm-yyy

# s = "12-05-2018"
# r = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
# l = re.findall(r,s)
# print(l)

# s = "12-05-2018"
# r = re.compile("^(?P<date>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")
# m = re.search(r,s)
# if m:
# 	# print(m.group(2))
# 	print(m.group("year"))
# else:
# 	print("Pattern not found")


# s = "+91 8123456789"
# # s = "8123456789"
# # \s es para espacio
# r = re.compile("(?:\+91\s)?([6-9][0-9]{9})")
# m = re.search(r,s)
# if m:
# 	print(m.group(1))
# else:
# 	print("Pattern not found")



[0-9] = \d
[^0-9] = \d

[a-zA-Z0-9]  = \w
\w

space = \s
\S