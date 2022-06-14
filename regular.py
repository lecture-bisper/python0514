import re

data = """
park 800905-1049118
kim  700905-1059119
"""

result = []

print(data)

print("-" * 5, "정규 표현식", "-" * 5)

# line = data.split("\n")
#
# print(line)
#
# word_line1 = line[1].split(" ")
# word_line2 = line[2].split(" ")
#
# print(word_line1)
# print(word_line2)

for line in data.split("\n"):
    word_line = []

    for word in line.split(" "):
        if len(word) == 14:
            word = word[:6] + "-" + ("*" * 7)

        if word != "":
            print(word)
            word_line.append(word)

    if line != "":
        result.append(word_line)

print(result)

print("\n", "=" * 10, "re 모듈 사용", "=" * 10, "\n")

p = re.compile("[a-z]+")

m = p.match("python")
print(m)

m = p.match("pyth4on")

if m:
    print("매치됨 : {0}, {1}, {2}, {3}".format(m.group(), m.start(), m.end(), m.span()))
else:
    print("매치되지 않음 : {0}".format(m))


m = p.search("3  python")
print(m)
print(m.group())






