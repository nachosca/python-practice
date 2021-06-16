# l = [100,200,300,400,500]

# i = iter(l)
# # print(i)
# # print(next(i))
# # print(next(i))

# for x in i:
# 	print(x)


import itertools

# l1 = [10,20,30,40,50]
# l2 = [x*10 for x in l1]
# l3 = [x*10 for x in l2]

# i = itertools.chain(l1,l2,l3)
# print(i)
# print(next(i))
# for x in i:
# 	print(x)

# l = [10,20,30,40,50]
# count = 0
# for x in itertools.cycle(l):
# 	if count < 20:
# 		print(x)
# 	else:
# 		break
# 	count+=1

# l = [10,20,30,40,50]
# count = 0
# for x in itertools.repeat(l):
# 	if count < 20:
# 		print(x)
# 	else:
# 		break
# 	count+=1

# l = [10,20,30,40]
# i = iter(l)
# t = itertools.tee(i)
# print(t)

# for x in t[0]:
# 	print(x)

# for x in t[1]:
# 	print(x)


# l1 = [10,20,30,40,50]
# l2 = [x*10 for x in l1]
# l3 = [x*10 for x in l2]

# i = itertools.chain(l1,l2,l3)

# for x in itertools.islice(i,0,8):
# 	print(x)


# range(10,50)

# count = 0
# # se puede especificar el inicio, cada cuanto aumenta. pero no el final del count
# for x in itertools.count(10,3):
# 	if count > 20:
# 		break
# 	else:
# 		print(x)
# 	count+=1



l = [1,2,3]
print(list(itertools.permutations(l,2)))
print(list(itertools.combinations(l,2)))