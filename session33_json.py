# json objects  dict {"key": "value"}
# numbers 10 - 10.55 int - float
# array [10,"string"] list
# 					tuple
# " "					'' "" """  """


import json

handle = open("json_input.json", "r")
content = handle.read()

handle.close()

# print(content)
d = json.loads(content)
print(d)
print(d["database"])
print(d["database"]["port"])

d["database"]["port"] = 3330

print(d["database"]["port"])
print(d["files"])
print(d["files"]["log"])
d["files"]["log"] = ("/log/app.log", "log/mysql/app.log")

print(d)

j = json.dumps(d,indent=4,sort_keys=True)
print(j)
handle = open("json_output.json", "w")
handle.write(j)
handle.close()