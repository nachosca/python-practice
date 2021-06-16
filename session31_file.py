# r  read
# r+
# w write
# w+
# a append
# a+
# fp = open("input.txt","r")
# content = fp.read()
# print(content)

# print("-------------------------------------")

# content = fp.read()
# print(content)


# content = fp.read(25)
# print(content)


# readlines
# readline

# content = fp.readlines()
# print(content[:5])

# content = fp.readline()
# print(content)
# content = fp.readline()
# print(content)
# content = fp.readline()
# print(content)
# content = fp.readline()
# print(content)


# for x in fp:
# 	print(x)
# offset => number of chars
# position -> 0 start of file
# 			1 current position
# 			2 eof

# seek(15,0) -> change de fp by 15 chars from start of the file
# seek(0,2) -> change fp by 0 chars from oof
# seek(15,1)
# seek(15,2)

# fp = open("input2.txt","w+")
# print(fp.tell())
# fp.write("Sample text line 1")

# print(fp.tell())

# content = fp.read()
# print(fp.tell())
# print(content)
# fp.seek(0,0)
# content = fp.read()
# print(fp.tell())
# print(content)


# tell -> current fp position
# seek -> change file pointer

# w+ => read + write - pisa el archivo y lo podés leer
# r+ => read + write - lees el archivo, mantiene el archivo y lo podés editar



# fp = open("input.txt", "r+")
# content = fp.read()
# print(content)

# fp.write("\n\nSample line added usint py script")
# content = fp.read()
# print(content)


# a
# a+

# r,r+,w,w+, => fp is at start
# a, a+ => at the end

# fp = open("input.txt", "a+")

# fp.write("\n\nabc")


# r => fp - start, file should exist, read.
# r+ => fp - start, file should exist, read + write

# w => fp - start, create a new file, write
# w+ => fp - start, create a new file, write + read

# a => fp - end, create a new file, write at end
# a+ => fp - end, create a new file, write at end + read

