number = int(input())
names_set = set()

for i in range(number):
    name = input()
    names_set.add(name)

[print(x) for x in names_set]