

str = set()

str.add((5, 3))
str.add((5, 2))
str.add((5, 1))

print(str)

for i in str:
    if 5 == i[0]:
        print("Yes")
