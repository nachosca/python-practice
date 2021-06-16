# dict:
# - mutable
# - unordered
# - keys are unique
# - keys should be immutable, int, str float, tuple

# crea un hash table.
# time O(1)

d = {"emp_id":101,"name":"ABC","email":"abc@gmail.com"}

print(d)

# d["contact_num"] = 1234567891
# print(d)

# d["contact_num"] = 12341234
# print(d)

# print(d["name"])

# get
# setdefault

# print(d.get("age", -1))
# print(d.get("emp_id", "Emp no exist"))

# print(d.setdefault("age", 50))
# print(d)


# for key in d:
# 	print(key, d[key])


# 1:1, 2,3:4

# d = {}
# for x in range(1,11):
# 	d[x] = x*x
# print(d)

# print(d.keys())
# print(d.values())
# print(d.items())

for t in d.items():
	print(type(t))
