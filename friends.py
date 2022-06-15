import re

f = open("friends101.txt", "r", encoding="utf-8")

script101 = f.read()
f.close()

print(script101[:100])

line = re.findall(r"Monica:.+", script101)

for item in line[:3]:
    print(item)

name = re.compile(r"[a-zA-Z]+:")
names = re.findall(name, script101)
print(names)

print(set(names))
name_list = list(set(names))

print(name_list)
