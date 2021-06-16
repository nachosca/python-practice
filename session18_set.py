#sets:
# - sets are mutable
# - all the elements should be unique
# - add immutable elements in the set: int float tuple str
# - unordered


# s = {10,20,30,40}
# print(s,type(s))

# s = {100,200,300,400}

# s.add(500)
# print(s)

# s1 = {10,20,30,40,50,60}
# s2 = {40,50,60,70,80,90}

# s3 = s1.union(s2)
# print(s3)

# s3 = s1.intersection(s2)
# print(s3)

# s3 = s1.difference(s2)
# print(s3)

# s3 = s2.difference(s1)
# print(s3)

# s3 = s1.symmetric_difference(s2)
# print(s3)

# print(s1)
# s1.update(s2)
# print(s1)

# s1.intersection_update(s2)
# print(s1)

# s1.difference_update(s2)
# print(s1)

# s1.symmetric_difference_update(s2)
# print(s1)

# s1 = {100,200,300,400,500}
# s2 = {100,200,300}

# print(s2.issubset(s1))
# print(s1.issuperset(s2))


# l = [100,200,300,400,400,500,500]

# s = set(l)
# print(s, l)

# l1 = [100,200,300,400,500]
# l2 = [50,100,150,200,250,500,45,35,10]

# s1 = set(l1)
# s2 = set(l2)

# s3 = s1.union(s2)
# print(s3)

# l3 = list(s3)

# print(l3)
# l3.sort()
# print(l3)


# l3 = sorted(s3)
# print(l3)


# pop
# remove
# discard
# clear
# del


s = {100,200,300,400,500,600}
# r= s.pop(100)
# print(s,r)

# s.remove(100)
# print(s)

s.discard(1000)
print(s)

s.clear()
print(s)