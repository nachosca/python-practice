# l = [100,200,300,400,500]
# l2 = [value*value for value in l]
# print(l2)

# for x in l:
# 	l2.append(x*x)

# print(l2)




# l = [10,20,25,30,35,60,65,70,85]
# l2 = [x for x in l if x%2 == 0]
# print(l2)

# l = ['abc','abcd','abcde','zzzzzz']
# l2 = [len(x) for x in l]
# print(l2)

# l2 = [(x1,x2) for x1 in range(1,5) for x2 in range(100,103)]
# print(l2)

# l = [[1,2,3],[4,5,6],[7,8,9]]
# l2 = [x2 for x in l for x2 in x]
# # for value in l:
# # 	for val2 in value:
# # 		l2.append(val2)

# print(l2)

# l = [100,105,110,115,120]
# # "even", odd
# l2 = ["Even" if x%2 ==0 else "Odd" for x in l]
# print(l2)


# # 1:1,2:4,3:9,4:16
# d = {x:x**2for x in range(1,11)}
# print(d)


# 'a':97, 'b':98, 'c':99, ...z"122
d = {chr(x):x for x in range(97,123)}
# print(d)

d2 = {x:y for x,y in d.items()}
print(d2)