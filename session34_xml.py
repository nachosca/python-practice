import xmltodict

handle = open("xml_input.xml", "r")

content = handle.read()
# print(content)


d = xmltodict.parse(content)
print(d["Result"]["RequestCode"])

d["Result"]["RequestCode"] = 4 

# print(d)

x = xmltodict.unparse(d)
print(x)